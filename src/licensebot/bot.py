from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from licensebot.decision import Decision

msg_b = "Since you contacted me, i figure you want me to help you choosing a license?"

# Replace with your decision_handler instance
# from your_decision_handler_module import decision_handler


class TelegramBot:
    decision_handler: Decision
    application: Application
    # We'll use a constant for our conversation state.
    conversation_state = 0

    def __init__(self, token: str, decision_handler: Decision) -> None:
        self.decision_handler = decision_handler
        # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token.
        self.application = Application.builder().token(token).build()

        # Define the conversation handler with the states.
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                self.conversation_state: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        self.receive_answer,
                    ),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )
        self.application.add_handler(conv_handler)

    def start_bot(self) -> None:
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

    async def start(self, update: Update, context: CallbackContext) -> int:
        """Start the conversation and ask the first question."""
        await update.message.reply_text(
            "Hi, I'm the license bot. I'm here to guide you through your decision "
            "making process when choosing a license for your open source project.",
        )
        state = self.decision_handler.state()
        if state.is_leaf:
            # If we're already at a leaf, return the result.
            await update.message.reply_text(
                f"Your License: {state.title}\n{state.body}",
            )
            return ConversationHandler.END
        return await self.ask_question(update, context)

    async def ask_question(self, update: Update, context: CallbackContext) -> int:
        """Sends the current question and options to the user."""
        state = self.decision_handler.state()
        text = f"*{state.title}*\n\n{state.body}\n\n*Options:*"

        # Build a mapping from branch to child and a keyboard list.
        children = {child.branch: child for child in state.children}
        keyboard = []
        for branch, child in children.items():
            if child.is_leaf:
                option_text = f"{branch} ---> {child.title}"
            else:
                option_text = f"{branch} ---> next question: {child.title}"
            text += f"\n{option_text}"
            # We use the branch as the reply key.
            keyboard.append([branch])

        # Send message with markdown formatting and a keyboard for options.
        await update.message.reply_text(
            text,
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
            parse_mode="Markdown",
        )
        return self.conversation_state

    async def receive_answer(self, update: Update, context: CallbackContext) -> int:
        """Handles the user's answer and moves the tree to the next state."""
        answer = update.message.text.strip()
        self.decision_handler.next(answer)
        state = self.decision_handler.state()

        if state.is_leaf:
            await update.message.reply_text(
                f"Your License: {state.title}\n\n{state.body}",
                reply_markup=ReplyKeyboardRemove(),
            )
            return ConversationHandler.END
        return await self.ask_question(update, context)

    async def cancel(self, update: Update, context: CallbackContext) -> int:
        """Cancels and ends the conversation."""
        await update.message.reply_text(
            "Conversation canceled.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

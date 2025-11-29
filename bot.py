from telegram.ext import Application, MessageHandler, filters
import asyncio

async def forward_handler(update, context):
    await context.bot.send_message(-1003342577939, "پیام جدید: " + update.channel_post.text)

app = Application.builder().token("8270404319:AAGFjjgCPaQxJztnAGodVeaa8Oz5il2UNeE").build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, forward_handler))
app.run_polling()

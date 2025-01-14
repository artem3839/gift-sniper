class Text:
    start = '<b>👋 Привет, {user}!</b> С помощью данного бота вы можете организовать автоматическую покупку новых <b>Telegram Gifts</b>.'
    profile = (
        '<b>📄 Профиль пользователя {user}</b>\n\n'
        '<b>- ID: </b><code>{id}</code>\n'
        '<b>- Баланс: </b><code>{balance}</code> ⭐\n'
        '<b>- VIP:</b> {status_vip}\n\n'
        '<i>С VIP-подпиской интервал проверки новых подарков сокращается с <b>{default_interval}</b> до <b>{vip_interval}</b> секунд!</i>'
    )
    get_amount = '<b>💳 Введите сумму пополнения баланса в ⭐</b>'
    invoice_emoji = '🌟'
    success_invoice_emoji = '🥳'
    successful_invoice = '<b>✅ Ваш баланс был пополнен, для настройки автоматической покупки подарков перейдите в пукнт <i>Информация</i></b>'
    
    class errors:
        not_integer = '<b>❌ Пожалуйста введите целое число</b>'
        invoice_reject = "Счет на пополнение баланса уже недействителен"

    class utils:
        bool_to_emoji = lambda status: '✅' if status else '❌'
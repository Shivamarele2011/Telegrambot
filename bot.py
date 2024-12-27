import yfinance as yf
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Function to get stock data from Yahoo Finance
def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_info = stock.info
    
    # Extracting relevant information
    data = {
        'Stock Name': stock_info.get('shortName', 'N/A'),
        'Current Price': stock_info.get('regularMarketPrice', 'N/A'),
        'Market Cap': stock_info.get('marketCap', 'N/A'),
        'P/E': stock_info.get('trailingPE', 'N/A'),
        'Book Value': stock_info.get('bookValue', 'N/A'),
        'Dividend Yield': stock_info.get('dividendYield', 'N/A'),
        'ROE': stock_info.get('returnOnEquity', 'N/A'),
        'ROCE': stock_info.get('returnOnAssets', 'N/A'),
        'Industry PE': stock_info.get('industry', 'N/A'),
        'Intrinsic Value': 'N/A',  # Intrinsic value calculation requires an additional method.
    }
    
    return data

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your stock info bot. Type /stock <symbol> to get stock information.')

# Stock command to fetch stock info
def stock(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text("Please provide a stock symbol. For example: /stock AAPL")
        return
    
    stock_symbol = context.args[0].upper()
    stock_data = get_stock_data(stock_symbol)
    
    # Prepare the response message
    response = f"Stock Information for {stock_symbol}:\n"
    for key, value in stock_data.items():
        response += f"{key}: {value}\n"
    
    update.message.reply_text(response)

def main() -> None:
    # Replace '7748316171:AAHMhEi7otOI40knNpZjR7cv6CtACZZnZwM' with your actual Telegram Bot API token
    updater = Updater("7748316171:AAHMhEi7otOI40knNpZjR7cv6CtACZZnZwM")

    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stock", stock))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()

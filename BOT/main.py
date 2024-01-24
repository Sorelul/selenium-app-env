from book.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
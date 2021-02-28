import connexion 
from connexion import NoContent

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from stock_open_price import StockOpenPrice
from stock_news import StockNews
import datetime


DB_ENGINE = create_engine("sqlite:///readings.sqlite")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def read_stock_open_price(body):
    """ Receives a stock open price reading """

    session = DB_SESSION()

    open_price = StockOpenPrice(
                       body['stock_code'],
                       body['price'],
                       datetime.datetime.strptime(body["date"], '%Y-%m-%d %H:%M:%S.%f'),)

    session.add(open_price)

    session.commit()
    session.close()
    return NoContent,201

# def read_stock_close_price(body):
#     print(body)
#     return NoContent,201

def read_stock_news(body):
    """ Receives a stock news reading """

    session = DB_SESSION()

    stock_news = StockNews(
                   body['stock_code'],
                   body['news'],
                   body['source'],
                   datetime.datetime.strptime(body["date"], '%Y-%m-%d %H:%M:%S.%f'))

    session.add(stock_news)

    session.commit()
    session.close()

    return NoContent,201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml",strict_validation=True,validate_responses=True)

if __name__ == "__main__":
    app.run(port=8090)
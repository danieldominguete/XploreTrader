from src.lib.data_aquisition.financial_data import GetFinancialData
from src.lib.utils.util import save_json, save_csv

# Parameters
stock = "GOOG"
source = "yahoo_finance"
period = "max"

# Get data from web
data_gateway = GetFinancialData(source=source)

test = data_gateway.get_asset_info(asset=stock)
save_json(data=test, filename="company.json")

test = data_gateway.get_historical_data(asset=stock, period=period)
save_csv(data=test, filename="stock.csv")

# test = data_gateway.get_asset_cashflow(asset=stock)
#
# test = data_gateway.get_asset_balance_sheet(asset=stock)
#
# test = data_gateway.get_asset_earnings(asset=stock)
#
# test = data_gateway.get_asset_financials(asset=stock)
#
# test = data_gateway.get_asset_holders(asset=stock)
#
# test = data_gateway.get_asset_quarterly_balance_sheet(asset=stock)
#
# test = data_gateway.get_asset_quarterly_cashflow(asset=stock)
#
# test = data_gateway.get_asset_quarterly_earnings(asset=stock)
#
# test = data_gateway.get_asset_quarterly_financials(asset=stock)
#
# test = data_gateway.get_asset_sustainability(asset=stock)
#
# test = data_gateway.get_asset_recommendations(asset=stock)
#
# test = data_gateway.get_events_calendar(asset=stock)

print("bye!")


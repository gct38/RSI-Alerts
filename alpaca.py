def get_watchlist_symbols(watchlist_name, api):
    id = api.get_watchlist_by_name(watchlist_name).id
    watchlist = [x['symbol'] for x in api.get_watchlist(id).assets]
    return watchlist

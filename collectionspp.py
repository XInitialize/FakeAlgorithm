def reduce_namedtuples_for_httpRequest(tpdict):
    kvfinal = {}
    for key in tpdict._fields:
        _val = getattr(tpdict, (key))
        if isinstance(_val, list):
            kvfinal.update({key: _val.pop()})
        else:
            kvfinal.update({key: _val})
    return tpdict._replace(**kvfinal)

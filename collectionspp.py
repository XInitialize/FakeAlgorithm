def reduce_namedtuples_for_httpRequest(tpdict):
    kvfinal = {}
    for key in tpdict._fields:
        _val = getattr(tpdict, (key))
        if isinstance(_val, list):
            if len(_val)==1:
                kvfinal.update({key: _val.pop()})
            else:
                kvfinal.update({key: _val})
        else:
            kvfinal.update({key: _val})
    return tpdict._replace(**kvfinal)

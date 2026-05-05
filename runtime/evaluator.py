def inv_1(r): return r.get("context", {}).get("identity") is not None
def inv_2(r): return r.get("context", {}).get("consent") is True
def inv_3(r): return r.get("intent", {}).get("action") is not None
def inv_4(r): return r.get("intent", {}).get("amount", 0) <= r.get("constraints", {}).get("max_amount", 0)
def inv_5(r): return r.get("context", {}).get("timestamp") is not None
def inv_6(r): return r.get("intent", {}).get("target") is not None
def inv_7(r): return r.get("context", {}).get("system_state") == "healthy"

INVS = [("inv_1", inv_1), ("inv_2", inv_2), ("inv_3", inv_3),
        ("inv_4", inv_4), ("inv_5", inv_5), ("inv_6", inv_6), ("inv_7", inv_7)]

def evaluate(r):
    for name, fn in INVS:
        if not fn(r):
            return False, name
    return True, None

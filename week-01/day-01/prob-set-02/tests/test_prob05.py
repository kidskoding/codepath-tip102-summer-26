from prob05 import concatenate

def test_prob05():
    assert concatenate(["vengeance", "darkness", "batman"]) == "vengeancedarknessbatman"
    assert concatenate([]) == ""

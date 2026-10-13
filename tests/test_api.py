def test_exp(client)
    resp=client.get("/")
    assert resp.headers["X-Visites-Version"]=="0.1.0"

def test_raz(client):
    client.get("/")
    client.get("/")
    resp=client.post("/reset")
    assert resp.json()=={"visites":0}
    assert client.get("/").json()=={"visites":1}

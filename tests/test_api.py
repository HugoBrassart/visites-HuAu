def test(client):
 client.get("/")
 client.get("/")
 resp=client.post("/reset")
 assert resp.json()=={"visites":0}
 assert client.get("/").json()=={"visites":1}

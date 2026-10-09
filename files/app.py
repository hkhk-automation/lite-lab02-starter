#!/usr/bin/env python3
"""Labori seis: väike veebirakendus kolmekihilise pinu harjutamiseks.

GET /        loeb külastuse andmebaasi ja näitab, mis masin vastas
GET /health  200, kui andmebaas vastab, muidu 503

Seaded tulevad keskkonnamuutujatest (systemd EnvironmentFile).
"""
import os
import socket
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import psycopg2

MASIN = socket.gethostname().split(".")[0]
NIMI = os.environ.get("APP_NIMI", "Labori seis")
VERSIOON = os.environ.get("APP_VERSIOON", "1.0")
PORT = int(os.environ.get("APP_PORT", "8080"))

# Harjutuse jaoks: versioon, mis lõpeb "-katki", ei käivitu (kodutöö H3).
if VERSIOON.endswith("-katki"):
    sys.exit(f"{NIMI} {VERSIOON}: vigane väljalase, ei käivitu")


def yhendus():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ["DB_NIMI"],
        user=os.environ["DB_KASUTAJA"],
        password=os.environ["DB_PAROOL"],
        connect_timeout=3,
    )


def kylasta():
    c = yhendus()
    try:
        with c, c.cursor() as k:
            k.execute(
                "CREATE TABLE IF NOT EXISTS kylastused ("
                " id serial PRIMARY KEY,"
                " masin text NOT NULL,"
                " aeg timestamptz NOT NULL DEFAULT now())"
            )
            k.execute("INSERT INTO kylastused (masin) VALUES (%s)", (MASIN,))
            k.execute("SELECT masin, count(*) FROM kylastused GROUP BY masin ORDER BY masin")
            return k.fetchall()
    finally:
        c.close()


class Kasitleja(BaseHTTPRequestHandler):
    def saada(self, kood, tekst):
        keha = tekst.encode("utf-8")
        self.send_response(kood)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(keha)))
        self.end_headers()
        self.wfile.write(keha)

    def do_GET(self):
        if self.path == "/health":
            try:
                yhendus().close()
                self.saada(200, f"ok {MASIN}\n")
            except psycopg2.Error as e:
                self.saada(503, f"andmebaas ei vasta: {e}".strip() + "\n")
            return

        read = [f"{NIMI} {VERSIOON}", f"Vastas: {MASIN}"]
        try:
            loendid = kylasta()
            read.append("Külastused: " + " ".join(f"{m}={n}" for m, n in loendid))
            self.saada(200, "\n".join(read) + "\n")
        except psycopg2.Error as e:
            read.append(f"Andmebaas: VIGA {e}".strip())
            self.saada(500, "\n".join(read) + "\n")


if __name__ == "__main__":
    print(f"{NIMI} {VERSIOON} kuulab pordil {PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Kasitleja).serve_forever()

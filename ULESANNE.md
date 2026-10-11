# Lab 02 — Kolmekihiline rakendus · ülesanne

**Loeng:** <https://hkhk-automation.github.io/devops-lite/week02/lecture/>
**Praktikum:** <https://hkhk-automation.github.io/devops-lite/week02/lab/>
**Kodune õpe ja kodutöö:** <https://hkhk-automation.github.io/devops-lite/week02/homework/>

See fail on ülesande kirjeldus, seda ei pea muutma. Klassitöö dokumenteerid failis **`README.md`**, mis on mall. Rollid ja `site.yml` ehitad ise praktikumi juhendi järgi.

---

## Mis repos alguses on

| Fail | Mis see on |
|---|---|
| `ansible.cfg` | sama mis K1-s |
| `files/app.py` | rakendus „Labori seis“, A3-s tõstad selle rolli `app` kausta `files/` |
| `host_vars/vm3.yml` | kolleegi jäetud erisus vm3-le, jäta alles |
| `vead/` | kodutöö H5 jaoks, ära kasuta klassitöös |

Eeldus: K1 osa B on tehtud (`ssh vm1`, `ssh vm2`, `ssh vm3` töötavad vm1-s võtmega, `ansible.posix` on paigaldatud).

---

## Mis peab lõpuks repos olema

**Klassis (praktikum):**

| Fail | Kust |
|---|---|
| `inventory.ini` | A1 |
| `group_vars/all.yml` | A2 |
| `site.yml` | A3–A6, B4 |
| `roles/common`, `roles/db`, `roles/app`, `roles/lb` | A3–A7 |
| `logid/site_teine_jooks.txt` | A8, B4 |
| `logid/vaheldumine.txt` | B1 |
| `logid/uks_maas.txt` | B3 |
| `README.md` täidetud | Esitamine |

**Kodus (kodune õpe ja kodutöö, vabatahtlik boonus):**

| Fail | Kust |
|---|---|
| `markmed.md`, `vastused.md` | I, H1, III |
| `logid/kolm_rakendust.txt` | H1 |
| `uuendus.yml`, `logid/uuendus.txt`, `logid/uuendus_curl.txt` | H2 |
| `logid/tagasi.txt` | H3 |
| `requirements.yml`, README jaotis „Käivitamine“ | H4 |
| `vead.md` | H5 |

---

## Kontrollnimekiri (Issues ja projekt)

Su repo **Issues** all on selle nädala issue **Lab 02 · Kolmekihiline rakendus**. Märgi ruut, kui osa on tehtud. Kui kõik on tehtud, sulge issue. Sama issue on kursuse projektis vaates **Minu tööd**.

Kui jääd kinni: **Issues → New issue → Vajan abi**. Juhendaja saab teate.

---

## Kontroll

Igal push'il jookseb automaatne kontroll **Autograde** (vahekaart **Actions**). Hinne: K1–K5 (45 p). Kodutöö on vabatahtlik boonus – punane rist Actionsis tähendab ainult, et boonus on tegemata.

| Kontroll | Punkte |
|---|---|
| K1–K5: failid ja README, süntaks, rollid ja inventar, mallid ja turve, tõendid | 45 |
| BOONUS H1 kolm rakendusserverit, H2 uuendus masinhaaval, H3 tagasipööramine | boonus |
| BOONUS H4 `requirements.yml`, H5 kolleegi vead | boonus |
| BOONUS I märkmed ja vastused | boonus |

Tõendi salvestad nii (failinimed on tabelis ülal):

```bash
ansible-playbook site.yml | tee logid/site_teine_jooks.txt
```

`changed=0` tuleb ainult siis, kui kõik on juba paigas. Seega salvesta **teine** jooks.

---

## Esitamine

```bash
git add . && git commit -m "Lab 02"
git push
```

Tähtaeg on kirjas Classroom 50-s. Pushida võid mitu korda, arvesse läheb viimane. Reposse ei lähe paroole, võtmeid ega Vaulti paroolifaili.

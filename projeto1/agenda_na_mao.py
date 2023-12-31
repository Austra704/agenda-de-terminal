AGENDA = {
    "guilherme": {
        "tel": "99999-1010",
        "email": "contato@solyd.com.br",
        "endereço": "av. 1"
    },
    "maria": {
        "tel": "99229-2020",
        "email": "maria@solyd.com.br",
        "endereço": "av. 2"
    },
    "joão": {
        "tel": "98267-6060",
        "email": "joão@solyd.com.br",
        "endereço": "av. 3"
    },
}

AGENDA['guilherme']['endereco'] = "Rua das nações"


AGENDA['lucas'] = {
    "tel": "98882-2189",
    "email": "lucas@solyd.com.br",
    "endereco": "av. josé bonifacio",
}

AGENDA.pop("guilherme")

for contato in AGENDA:
    print(contato)

print(AGENDA['lucas'])
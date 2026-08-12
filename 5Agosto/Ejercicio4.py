horarios={"Mañana":["7:30", "12:30"],
         "Tarde":["13:00","18:00"]}
for timbre in ("Mañana","Tarde"):
    print(f"Timbre: {timbre}")

    for horario in horarios[timbre]:
        print(f"Horario-{horario}")

        for sonido in range(1,3):
            print(f"Ring!{sonido}")
label cap1_evan:
    $ evan_counter += 1

    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    play music "audio/downtime.mp3" volume 0.25

    "Caminé hacia Evan de forma tímida" 
    
    "Yo no tenía una misión asignada, pero de quienes conocía Evan era quien me daba un poco de confianza a pesar de su aspecto y su forma seria de actuar."

    #show evan

    show evan lado2 at center with dissolve:
        zoom sprite_size

    a "Hola."

    e "¿Qué haces aquí?"

    "Evan parecía esconder algo en su bolsillo, quizás un poco nervioso por no esperarse mi presencia."

    a "Oh, es que, Freya no me dio una misión en particular por lo que... imaginaba que podría acompañarte en tu guardia."

    "Estaba curioso, e intenté ver lo que Evan guardó pero éste solo se movió un poco para ocultarlo más."

    show evan pensando with dissolve

    e "Ya veo, así que decidiste venir a husmear por acá."

    a "Ah, bueno, si es que no te molesta, claro."

    show evan normal with dissolve

    e "No, para nada, solo pensé que sería la última persona que querrías acompañar."

    a "¿Por qué dices eso?"
    
    show evan despair with dissolve

    e "Bueno, Freya por allá no es muy fan de mi forma de ser."

    a "¿Tú y Freya se conocían?"

    show evan ladobrazoenojado with dissolve

    e "Sí, pero no nos llevamos del todo bien."

    e "Digamos que su forma de ser es muy recta, tuvimos un trabajo por áreas hace bastante tiempo pero creo que no le gustó mi metodología de trabajo."

    a "¿Metodología?"

    show evan pensando with dissolve

    e "Decía que mi ética era incorrecta, inclusive intentó llevarme a una de sus clases para comprender su \"justicia\""

    a "Oh... ya veo... Pero, ¿tú qué piensas de ella?"

    show evan ceja with dissolve

    e "¿Ella? Bueno, es solo una molestia, personas como esas no llegarán muy lejos si siguen acertando sus creencias sobre otros sin importar lo que el otro piense."

    menu:
        "Supongo que tienes razón.":
            a "Supongo que tienes razón."

        "No lo sé...":
            a "No lo sé..."

        "Suena complicado.":
            a "Suena complicado."

    show evan normal with dissolve

    e "Pero... no es mala persona, lo sé, solo es bastante selectiva."

    a "Sí... Bueno, sería cuestión de conocerla para saber por qué actúa así."

    show evan ceja with dissolve

    e "Eso es raro..."

    a "¿Qué cosa?"

    show evan lado with dissolve

    e "Esos posters, no estaban así antes."

    "Evan caminó hacia la puerta donde varios posters estaban colocados sobre la pared."
    
    "Confundido, éste los observó."

    show evan ladobrazo with dissolve

    e "Se ven como símbolos y palabras extrañas."

    a "Tienes razón, pero es casi lo mismo que pasó con mi libro..."

    show evan pensando with dissolve

    e "Bueno, tampoco puedo leerlo así que... no tiene sentido verlo más..."

    a "S...si tu lo dices... supongo."

    stop music fadeout 0.75
    
    return

label cap1_freya:
    $ freya_counter += 1

    #bg cafateria

    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    play music "audio/downtime.mp3" volume 0.25

    "Claro que mi cuerpo entero temblaba, de hecho, la simple idea de acercarme a Freya aun no me agradaba del todo."

    "Aun así, tomando algo de valor de mi interior, caminé detrás de ella."

    "¿Hacer algo de provecho? Quizás podía ayudarla, ¿no?"

    #show freya

    show freya normal at center with dissolve:
        zoom sprite_size

    fr "Cuando dije \"algo de provecho\", me imagine que irías con alguien más..."

    "Estaba un poco helado, ¿qué se supone que debo decir en estas situaciones?"

    "Era evidente que darle la razón no me llevaría a ningún lugar."

    a "Supongo que... haré más buscando contigo..."

    "La chica bufó y me dio la espalda lanzando su cabello hacia atrás en forma de molestia."

    show freya ladohabla2 with dissolve

    fr "Bien, pero no te pongas en mi camino."

    #bg cocina

    scene bg cocina with fade

    "Freya comenzó a buscar entre los estantes principales de la cocina sacando varias cosas empaquetadas y revisando que estuviesen cerradas."

    "Descartaba cualquier alimento que estuviese al aire como frutas o verduras al igual que carne o cosas que tuvieran que prepararse."

    #hide freya

    hide freya with dissolve

    "A decir verdad, no sé mucho de supervivencia pero he leído uno que otro libro de apocalipsis zombie, así que de algo tenía que servir."

    menu:
        "Checar estantes superiores":
            "Subiéndome a una pequeña plataforma vi un par de cosas en la cima de las estanterías."

            "Parecían solo ser materiales para cocinar: harina, arroz, sal y azúcar."

            #show freya

            show freya lado at center with dissolve:
                zoom sprite_size

            "Bajé lentamente para no caerme y por un segundo vi a Freya quien pareció rodar los ojos con decepción."

        "Checar estantes inferiores":
            "Entre los estantes y los cajones que quedaban a la altura de mi cadera solo pude encontrar cubiertos viejos y usados, como si no los hubiesen lavado en años."

            "Intenté tomar un cuchillo del cual salió una cucaracha corriendo, o quizás una rata, no pude ver con claridad pues asustado lo tiré y cubrí mi boca para no gritar."

            scene bg cocina with vpunch

            a "¡AHHHH!"

            #show freya

            show freya caderaspreocupada at center with dissolve:
                zoom sprite_size

            "Freya bufó molesta al escuchar aquella acción."

        "Checar almacén":
            $ freya_counter += 1

            "Abrí una de las alacenas de metal que tenían al final de la cocina; ahí encontré muchas latas de comida."

            "Todas parecían intactas, o al menos la mayoría: atún, verduras; quizás lo suficiente para alimentar a una sola persona por un par de semanas."

            #show freya

            show freya sonrisahabla at center with dissolve:
                zoom sprite_size

            "Tomé un par y se las llevé a Freya, quien sonrió."

            fr "Vaya, no eres tan inútil."

            "Quizás no le agrado del todo, pero al menos se veía satisfecha."

    scene bg cocina with fade    

    show freya normalhabla with dissolve

    fr "Bueno, parece que ya buscamos aqui suficiente, ¿no lo crees?"

    "Tenía aún ese tono de superioridad al verme."

    "Corrían escalofríos por mi espalda como si no fuese capaz de enfrentarme a ella."

    a "Sí, eso creo."

    show freya caderassonrisa with dissolve

    fr "Bueno Arden, agradezco mucho tu cooperación, aunque claro, no la necesitaba desde un inicio."

    a "Ah... claro..."

    show freya normalhabla with dissolve

    fr "Te recomiendo que levantes la cabeza cuando hables con alguien, si no te veran como su presa."

    a "¿Cómo?"

    show freya apunta2 with dissolve

    fr "Levanta el mentón, echa los hombros hacia atrás. Si hablas tan bajo nunca te veran, y no creo que el mundo entero quiera a alguien más que dé lástima mientras camina."

    a "Oh..."

    "Eche mis hombros hacia atrás y alcé el rostro para poder verla con un poco más de seguridad, hubo una sonrisa de satisfacción en el rostro de Freya."

    show freya sonrisa with dissolve

    fr "Mucho mejor. No es tan difícil, ¿vez?" 
    
    fr "Vamos con el resto."

    "Freya no podrá ser la persona mas amistosa, pero... quizás logré acercarme un poco a ella."

    stop music fadeout 0.75

    return

label cap1_hanna:
    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    play music "audio/downtime.mp3" volume 0.25

    "Al no saber qué es hacer algo de provecho, seguí a la chica de cabello azul, quien se detuvo al ver que iba detrás de ella."

    #show hanna

    show hanna sonrisa at center with dissolve:
        zoom sprite_size

    h "Oh, hola..."

    a "Hey... Hanna, ¿cierto?"

    show hanna emocionadahabla with dissolve

    h "Sí, esa soy yo."

    a "¿Te molesta si te acompaño?"

    show hanna emocionada with dissolve

    h "No, para nada."

    "Después de negar con la cabeza, ambos empezamos a caminar hacia la esquina de la cafetería donde habían múltiples papeles tirados."
    
    "Hanna se acerco para tocarlos y observarlos."

    show hanna normal with dissolve

    h "No creo que esto nos sirva."

    a "¿Por qué no?"

    show hanna explicando with dissolve

    h "Bueno, yo no puedo leerlos, ¿tú puedes?"

    a "A ver..."

    "Hanna me entregó la hoja, habían múltiples figuras y símbolos en los posters, como si fuesen inspirados en algun idioma antiguo o inclusive runas."

    "Había leído varios libros de fantasía e inclusive algunos en latin, pero nada se parecía a lo que estaba viendo."

    h "¿Y bien? ¿Puedes leerlo?"

    menu:
        "Intentar descifrarlo con lo que sé.":
            "Con lo poco que tenía de conocimiento intenté hacer sílabas con las palabras, incusive un balbuceo sería bueno en este momento."

            a "Creo que dice... ah... ¿Bestia?"

            show hanna emocionada with dissolve

            h "¿Bestia? ¿Como la bella y la bestia?"

            "Una pequeña risa salió de Hanna como si intentase hacer el ambiente más ameno, yo solo pude sonreirle de una pequeña forma sincera."

            show hanna miedohabla with dissolve

            h "Perdón, no debería estar bromeando... mejor sigamos buscando."

        "Inventar algo.":
            "Tomé algo de valor y pensando en múltiples libros pude formular algo en mi cabeza, algo que tuviese sentido."

            a "Los caminos... de... la vida... llevan aquí..."

            "Hanna me vio con incredulidad, quizás fulminándome un poco con la mirada, luego asintió con la cabeza un par de veces."

            show hanna normal with dissolve

            h "Bueno, supongo que no tienen por qué tener sentido, ¿cierto?"

            a "No... supongo que no."

            "¿Acaso me había salido con la mía diciendo una estupidez?"

            show hanna explicando with dissolve

            h "Tal vez podrías traducir todo, así se completa por completo, ¿no lo crees?"

            "Hanna volteó a verme con sus ojos retadores, como si esperase algo de mí."

            a "Claro..."

            show hanna emocionadahabla with dissolve

            h "¡AJÁ! Esa es la cara de un mentiroso."

            "Exclamó con una sonrisa valiente sintiéndose orgullosa."

            h "Fue un buen intento engañarme pero no lo lograrás, soy una experta viendo las mentiras de los demás."

            "Quizás sonaba excesivamente confiada ahora."

            show hanna sonrisa with dissolve

            h "Mejor sigamos investigando."

        "Negarlo.":
            "Negué con la cabeza un par de veces admitiendo que no podía leer lo que decía en aquel folleto."

            show hanna normal with dissolve

            h "Bueno, sería muy bueno para ser verdad, mejor sigamos buscando."

    #bg cafeteria (algun fade)

    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    "Después de un buen rato de búsqueda no parecimos encontrar nada, Hanna volteaba a verme constantemente como si quisiese asegurarse de que estuviera bien."

    #show hanna

    show hanna miedohabla at center with dissolve:
        zoom sprite_size

    h "Hey... Arden... Ese... collar... ah..."

    hide hanna with dissolve

    show collar with dissolve:
        pos (0.5, 0.5) yanchor 0.5 xanchor 500 zoom 0.47

    a "Oh... me lo dio Katherine..."

    "Respondí de una forma evasiva viendo al suelo."

    h "¡Ah! Lo siento... no sabía que ella te lo había dado... quería decirte que... es realmente hermoso."

    a "¿Lo crees?"

    hide collar with dissolve

    show hanna sonrisa with dissolve

    h "Sí... me gusta mucho, quizás cuando salga le consiga uno a Freya. No le gusta admitirlo pero le facina la joyería, aunque casi no la use."

    a "¿Por qué no la usa?"

    show hanna explicando with dissolve

    h "Dice que la hace verla menos seria... Pero, a mí me gustaría que la usara más seguido, se ve linda con ella."

    a "Oh... bueno... seguro si se lo dices la usará más."

    show hanna emocionada with dissolve

    h "¿Tú crees?"

    a "Vale la pena intentarlo, supongo..."

    "Hanna pensó por un momento y luego asintió con la cabeza de forma decidida."

    show hanna emocionadahabla with dissolve

    h "Cuando salgamos de aquí, le compraré un collar y unos aretes... y... le diré que se los ponga diario, o... ¡dejaré de ser su amiga!"

    a "Creo que no hay que ser tan extremos."

    "Hanna negó con la cabeza como si esa fuese la única solución y siguió balbuceando sobre el tipo de joyería que le compraría a Freya; sin duda parecian ser muy buenas amigas."

    stop music fadeout 0.75

    return

label cap1_felix:
    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    "Nadie parecía tan confiable como Felix."

    #show felix

    show felix sonrisahabla at center with dissolve:
        zoom sprite_size
    
    "Tenía una gran sonrisa en su rostro mientras se alejaba del grupo y, al ver que me quedé parado viendo a los demás, se acercó a mí."

    f "Hey, ¿quieres venir conmigo? Seguro me harán falta un par de manos."

    a "Ah... sí, suena bien..."

    #bg cafeteria

    scene bg beast2 with fade

    play music "audio/flowerbloom.mp3" volume 0.19

    "Felix y yo caminamos en dirección contraria al resto, viendo por la ventana los jardines por donde merodeaba la criatura."

    "Su mandíbula cubierta de sangre mientras olfateaba, sus filosas garras que golpeaban el piso mientras caminaba..."
    
    "Ambos nos alejamos y escondimos debajo de la misma ventana."

    scene bg cafeteria with Fade(0.3, 0.1, 0.3):
        zoom 1.5 yalign 0.5 xalign 0.5

    #show felix

    show felix preocupado at center with dissolve:
        zoom sprite_size

    "Felix cubrió su boca un segundo antes de voltear a verme."

    f "Es aterrador, ¿no lo crees?"

    "¿Cómo no iba a serlo?"

    "¿Cómo es que aquel chico se mantenía en tanta calma a pesar de la situación en la que estabamos?"

    "¿Quizás estaba intentando ignorar que estaba asustado?"

    a "S...Sí, realmente lo es..."

    show felix manofrentepreocupadohabla2 with dissolve

    f "No puedo imaginar el miedo que pasó Katherine cuando fue devorada..."

    "Me detuve un segundo a pensarlo..."

    "Mis manos se escondieron en los bolsos de mi pantalón buscando algo de confort en el cual podría distraerme, pero no encontré nada."

    show felix pensando with dissolve

    f "Si hubieras podido tomar su lugar, ¿lo hubieras hecho?"

    menu:
        "No creo... poder tomar su lugar.":
            a "No creo... poder tomar su lugar."

            f "¿Por qué no lo crees? ¿Te aterra morir?"

            a "¿A ti no?"

            show felix ceja with dissolve

            f "Supongo... pero si tuviese a alguien tan cercano a mí sin duda tomaría su lugar."

            a "Regreso al momento en el que ocurrió y..."

            "Hice una ligera pausa antes de continuar."

            a "Creo que aunque pudiese hacerlo mi cuerpo se detendría, no es algo que yo pueda elegir."

            show felix pensando2 with dissolve

            f "Hmmm, interesante..."

        "Sí, lo haría si tuviese la oportunidad.":
            a "Sí, lo haría si tuviese la oportunidad."

            f "Claro, era tu mejor amiga después de todo, o al menos eso parecía."

            a "Éramos... muy cercanos."

            show felix sonrisa with dissolve

            f "Sí, creo que entiendo, también tomaría su lugar si tuviese la oportunidad."

        "No lo sé...":
            a "No lo sé..."

            f "Indeciso, ¿eh? ...Bueno, tampoco es algo que puedas tomar a la ligera... supongo... perder la vida..."

            a "Pareces muy cómodo hablando de eso."

            show felix pensandoceja with dissolve

            f "Bueno, no sé si me aterra morir realmente, quizás solo no de esa manera."

    a "Tú eras su novio, ¿cierto?"

    show felix sonrisahabla with dissolve

    f "¿Lo era? ¡Ah! Sí."

    "Una risa incómoda salió de su interior, quizás no debí de haber preguntado."

    f "Es que fue hace mucho tiempo, no nos odiabamos para nada, de hecho quedamos en buenos términos... solo que Kat solía ser muy... hmmm... sensible."

    a "Oh."

    "Yo recordaba que habían cortado hace un par de meses, a no ser que Katherine me haya mentido..."

    "No, estoy seguro de que fue quizás hace dos meses cuando cortaron, aún los veía saliendo a citas y todo..."

    "¿Quizás dos meses eran una eternidad para Felix?"

    show felix sonrisa with dissolve

    f "Sí, ya sabes cómo son las chicas. Como sea, no te habrá contado cosas malas de mí, ¿cierto?"

    a "Ah... no, no que yo recuerde..."

    show felix caderashabla with dissolve

    f "¿Ves? Soy una buena persona."

    "El chico se encogió de hombros soltando una pequeña risa"

    a "Sí..."

    "Algo me causaba incomodidad..."

    "Quizás el hecho de que no le parecía haber importado la muerte de Katherine, o quizás solo que era demasiado relajado."

    "Tal vez estaba viviendo esto de una forma... distinta."

    "¿Ignorando que la realidad existe?"

    "¿O siendo demasiado optimista?"

    "No puedo decifrarlo."

    stop music fadeout 0.75

    return
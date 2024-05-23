label cap2normal_evan:
    scene bg salonclases with Fade(0.3, 0.1, 0.3)

    play music "audio/downtime.mp3" volume 0.25

    "Evan se veía mal después de aquello, seguía en el suelo acostado."

    "Me agaché para estar a su nivel, se veía extremadamente cansado."

    #show evan

    show evan normal at center with dissolve:
        ypos 1.29 

    a "Ah..."

    show evan gimmeenojado with dissolve

    e "Ni lo menciones..."

    menu:
        "Lo lamento, puedo irme si quieres.":
            a "Lo lamento, puedo irme si quieres."

            show evan defensivo with dissolve

            e "N...no, está bien, solo..."

            "Evan suspiró viendose ligeramente incómodo."

            show evan normal with dissolve

            e "Creo que te debo una explicación..."

        "Necesito saber si estás bien.":
            a "Necesito saber si estás bien."

            show evan ladobrazoenojado with dissolve

            e "¡Estoy bien!"

            "Comenzó a toser de nuevo y se cubrió con el antebrazo."

            e "Ugh..."

            a "¿Estás... seguro que no necesitas ayuda?"

            "Evan se detuvo un momento y suspiró."

            show evan normal with dissolve

            e "Creo que necesitas una explicación."

    #show evan nomask

    show evan nmnormal with dissolve

    "Evan se volteó y se removió el cubrebocas, era una herida horrible y todavía tenía un poco de sangre en la boca por el encuentro con Freya, se veía horrible."

    e "Desde pequeño nací con... muchas enfermedades, de hecho es un milagro que siga vivo hasta la fecha..."

    show evan nmnormalhabla with dissolve

    e "Mi cuerpo es increíblemente debil y mi piel super sensible..."

    show evan nmladohabla with dissolve

    e "Mis padres me detestan por ello y solo descargan su energía en mí... supongo que... supongo que fue resultado de esto, la verdad no recuerdo bien porque caí inconciente."

    e "Mi cuerpo no sirve, soy demasiado débil... de hecho me cuesta mucho actividades que gente hace con naturalidad..."

    show evan nmnormalhabla with dissolve

    e "Tomo medicamentos y todo pero... obviamente no los tengo aquí... al menos... pensé que si iba al laboratorio encontraría un par pero... no..."

    a "Lo... lo lamento."

    show evan nmladohabla with dissolve

    e "Está bien, estoy acostumbrado a que me vean como el raro..."

    e "A decir verdad me hubiera gustado mucho haberlos ayudado en la barricada, y... de ser posible me hubiera encantado haber corrido a ayudar a Hanna... "
    
    extend "pero mi condición no me lo permite..."

    a "Ya veo... Y... ¿cómo te sientes ahora?"

    e "¿Cómo me siento?"

    e "Bueno... "

    show evan nmnormalhabla with dissolve
    
    e "Solo desesperanzado, supongo."

    show evan normal with dissolve

    a "Yo... no tengo mucho que ofrecerte pero, si puedo ser de ayuda en algo, por favor dímelo..."

    show evan feliz with dissolve

    e "Gracias, Arden."

    stop music fadeout 0.5

    return

label cap2normal_freya:
    scene bg salonclases with Fade(0.3, 0.1, 0.3)

    play music "audio/downtime.mp3" volume 0.25

    "La chica se veía con una sonrisa en su rostro, una muy pequeña que logré notar."

    "¿Quizás es por que estabamos haciendo lo que ella quería?"
    
    "Sí, eso tenía sentido."

    show freya normal at center with dissolve

    a "Hola..."

    show freya normalhabla with dissolve

    fr "Oh, tú, ¿no deberías estar haciendo algo de provecho?"

    a "Ah, bueno, es que..."

    show freya apunta with dissolve

    fr "¿No tienes a nadie más a quien molestar?"

    menu:
        "No quiero molestar, solo quería ver si necesitabas ayuda.":
            a "No quiero molestar, solo quería ver si necesitabas ayuda."

            show freya ladohabla2 with dissolve

            fr "Bueno, entonces ponte a hacer algo de provecho y no hagas preguntas ridículas, solo vamos a perder el tiempo así."

            show freya normalhabla with dissolve

            fr "Ayúdame a revisar las bancas de ahí."

        "Fuiste la primera persona con quien me topé...":
            a "Fuiste la primera persona con quien me topé..."

            show freya caderaspreocupada with dissolve

            fr "Vaya suerte, supongo que por eso estás aquí sin hacer nada..."

            "Tenía un tono molesto en su forma de hablar, se quedo viéndome un par de segundos antes de soltar un suspiro."

            show freya normalhabla with dissolve

            fr "¿Que tal si me ayudas a buscar en estas bancas ya que estás aquí?"

        "(Guardar silencio)":
            "No supe qué responder, para ser honestos su tono era bastante amenazante por lo cual solo me separé un poco de la mesa guardando silencio."

            show freya normalhabla with dissolve

            "Freya notó esto y se acomodó las gafas antes de hablar."

            fr "Bueno, ya que estás aquí supongo que puedes ayudarme a buscar entre las bancas."

    scene bg salonclases with fade

    "Asintiendo con la cabeza caminé hacia el estante mencionado buscando entre las bancas que se encontraban ahí, eran bancas normales."

    "Para ser honesto, sentía que estaba perdiendo el tiempo checando cada minúsculo detalle de ellas."

    "Al terminar de verificar que estaban vacías, volví con Freya."

    show freya normal at center with dissolve

    a "¿Encontraste algo?"

    show freya caderaspreocupada with dissolve

    fr "No realmente."

    fr "¿Tú tuviste más suerte?"

    "Negue con la cabeza soltando un pequeño suspiro avergonzado."

    show freya pensarhabla with dissolve

    fr "Hmmm, quizás no estamos buscando en el lugar indicado."

    a "¿Dónde suguieres, que... ah, busquemos?"

    show freya ladohabla2 with dissolve

    fr "A decir verdad, no lo sé."

    "Intentó verse segura pero su mirada se perdió un poco alrededor."

    show freya normal with dissolve

    fr "Sigamos buscando, no hay que perder la esperanza."

    a "Claro."

    stop music fadeout 0.5

    return

label cap2normal_hanna:
    scene bg salonclases with Fade(0.3, 0.1, 0.3)

    play music "audio/downtime.mp3" volume 0.25

    "Sentí que Hanna necesitaba compañía, así que fui con ella."
    
    "Al verme, una sonrisa sincera se formó en su rostro."

    #show hanna

    show hanna normal at center with dissolve

    h "¿No piensas investigar solo?"

    a "Ah, puedo irme si te molesta..."

    show hanna miedohabla with dissolve

    h "No, nada de eso, pensé que nunca te acercarás a mí, bueno, es difícil siendo que Freya siempre está de mi lado."

    a "Oh, cierto, bueno, no creo que sea por eso..."

    h "No es mala persona solo, hace lo que cree que es mejor para todos, tiene miedo de perder a más gente."

    a "¿A qué te refieres?"

    show hanna explicando with dissolve

    h "Bueno... hay personas que intentan hacer lo correcto de forma equivocada, solo que... ella se esfuerza mucho por mantener sus ideales y su vida recta, no tiene muchos amigos por eso."

    menu:
        "Creo que es muy directa.":
            a "Creo que es muy directa."

            show hanna normal with dissolve

            h "Oh... sí, sí lo es, pero no busca herir a nadie."

        "Me asusta un poco su forma de ser.":
            a "Me asusta un poco su forma de ser."

            show hanna normal with dissolve

            h "Sí, supongo que su forma de ser causa que la gente se asuste... pero no lo hace con mala intención."

        "No la conozco lo suficiente supongo...":
            a "No la conozco lo suficiente supongo..."

            show hanna sonrisa with dissolve

            h "Ojalá puedas conocerla algún día, para que comprendas el por qué es así."

    show hanna sonrisa with dissolve

    "Quizás Hanna conocía a otra persona, por que para mí esto no tenía nada de sentido."

    "Freya era muy grosera con todos y no podía justificar muchas de sus acciones."

    "Aun así me causaba curiosidad cómo es que dos personalidades tan distintas se habían conocido."

    a "Y... ¿cómo la conociste tú?"

    show hanna emocionada with dissolve

    h "Ah, ¿Freya?"

    h "Oh, eso fue hace mucho tiempo."

    show hanna explicando with dissolve

    h "Nos conocimos en la escuela antes de la universidad, creo que yo era muy introvertida en ese entonces..."

    h "No solía salir de mi recámara por días y tampoco tenía muchos amigos, lo único que me gustaba era el deporte, en ese entonces estaba entrenando artes marciales."

    a "¿Artes marciales? Debes de ser una especie de ninja."

    show hanna sonrisa with dissolve

    "Hanna río cuando escucho aquello."

    h "Me gustaría serlo, quizás en el futuro."

    show hanna emocionadahabla with dissolve

    h "Como sea, ella entró tarde a la escuela, era muy callada y los chicos de mi salon no querían conocerla, quizás porque era muy ruda y agresiva."

    h "A mí no me solían molestar por mi desempeño en el deporte, así que... un día, ella fue a verme a mi presentación."

    h "Fue la única persona del salón que fue... Se acercó a mí y me pidió ser su amiga... Desde ahí hemos sido inseparables."

    a "Suena muy lindo..."

    show hanna sonrisa with dissolve

    h "Lo es... Es una pena que nadie la comprenda... yo espero pueda hacer más amigos."

    "Yo vi eso imposible, quizás nadie veía a Freya como Hanna."

    a "Así que... artes marciales... cómo es que..."

    show hanna miedohabla with dissolve

    h "¿Soy tan miedosa?"
    
    h "Bueno... Todos tenemos miedos que sobrepasan nuestras capacidades... Creo que esta situación me pone muy nerviosa porque no sé cómo lidiar con ella."

    a "Sí, tiene sentido."

    "Después de la pequeña platica me aleje de ella para seguir investigando."

    stop music fadeout 0.5

    return

label cap2normal_felix:
    scene bg salonclases with Fade(0.3, 0.1, 0.3)

    play music "audio/downtime.mp3" volume 0.25

    #show felix

    show felix pensando at center with dissolve

    "Felix se quedó en el centro de la habitación, caminaba casi que en círculos viendo las estanterias y las mesas que estaban ahí para estudiar, sus ojos puestos casi en un vacío que no podia comprender."

    a "Hey..."

    show felix sonrisahabla with dissolve

    f "¡Oh! Arden."

    "Volteó a verme ladeando la cabeza ligeramente."

    a "Ah, ¿qué haces?"

    f "Oh, solo veía... el lugar, ya sabes, a veces hay cosas que no podemos comprender o ver."

    a "Lo esencial es invisible a los ojos."

    show felix ceja with dissolve

    f "¿Qué?"

    a "Ah, perdón, es una frase del principito, significa... bueno... da igual, es muy conocida mundialmente."

    show felix pensandohabla with dissolve

    f "Oh... Creo que no he escuchado de ese libro."

    a "¿N...No? Es un libro muy famoso, hay mercancía de él por todos lados."

    f "¿El principito?"

    a "Sí... Escrito por autor Antoine de Saint-Exupéry... ¿francés? Es un niño... ah... Vive en un planeta pequeño... cuida de una rosa..."

    "No sabiía cómo explicarle todo el libro en palabras sencillas, con lo que dije debía ser suficiente, pero no, Felix parecia verme desconcertado, quizás no es ley que todo el mundo lo conozca."

    a "Bueno, no importa, podríamos entonces revisar esta área..."

    show felix normal with dissolve

    f "Sí..."

    #hide felix

    hide felix with dissolve

    "Caminé por las mesas y me asomé debajo de ellas, ¿podía haber algo escondido ahí?"

    "Sería poco usual, pero tendría sentido, este lugar está alterado..."
    
    "De repente sentí una respiración detrás de mí, o una presencia, mi cuerpo se tensó y lentamente voltee hacia atrás."

    #show felix

    show felix sonrisahabla at center with dissolve:
        zoom 3 yalign 0.3
    f "¿Encontrasate algo?"

    a "N...No..."

    show felix pensandoceja with dissolve

    f "Quizás no hay nada por aquí después de todo... bueno, será mejor buscar en otro lado, no hay que perder el tiempo aquí."

    a "Sí, tienes razón."

    stop music fadeout 0.5

    return
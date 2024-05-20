label cap2bad_evan1:
    $ hasTalked_Evan = True

    scene bg salonclases2 with fade

    "Evan veía la ventana y decidí acercarme lentamente."

    show evan normal at center with dissolve

    e "¿Vienes a culparme?"

    a "¿Qué? No, ¿por qué haría eso?"

    show evan ladobrazo2 with dissolve

    e "Por no ayudar en la barricada."

    "Claro, aquel chico se había quedado parado cuando detuvimos las puertas con mesas."

    menu:
        "No vengo a culparte, quería saber cómo estabas.":
            show evan ladobrazo with dissolve

            e "¿Cómo estoy?"

            "El chico hizo una pausa antes de continuar."

            show evan gimme with dissolve

            e "No creo que sea importante... ¿o sí? Debemos encontrar cómo salir."

            a "Ah... sí, supongo que sí..."

        "¿Por qué... no nos ayudaste?":
            show evan despair with dissolve

            e "Yo... ah... no podía aunque quisiera."

            a "¿Por qué?"

            show evan pensando with dissolve

            e "Yo... soy demasiado débil, a pesar de mi altura y mi complexión... "

            show evan despair with dissolve

            extend "No puedo hacer mucho."

            a "¿Es... una enfermead?"

            show evan normal with dissolve

            e "Algo así..."

        "(No decir nada)":
            $ canKeepTalk_Evan = False

            show evan gimmeenojado with dissolve

            e "No dices nada, ¿eh?"

            a "Creo que..."

            e "Está bien... "
            
            extend "No te preocupes... "
            
            show evan ladobrazo with dissolve

            extend "no hace falta que lo intentes..."

            show evan ladobrazoenojado with dissolve

            e "Tampoco esperaba que alguien como tú lo entendiese."

            hide evan with dissolve

            "El chico se dio la vuelta y caminó a la otra esquina."

            return

    show evan normal with dissolve

    e "¿Y cuál es el plan ahora?"

    a "Supongo que sobrevivir..."

    show evan ladobrazo with dissolve

    e "Nada que no haya hecho antes... solo tiene un par de pasos extra..."

    a "¿A qué te refieres?"

    show evan gimmeenojado with dissolve

    e "Mi cuerpo... yo no debería estar vivo..."

    show evan ladobrazo with dissolve

    e "Tengo muchas complicaciones y debo ir al hospital muy seguido... "
    
    show evan ladobrazo2 with dissolve
    
    extend "supongo que solo es añadirle una raya al tigre..."

    a "¿Y... cómo vas con eso?"

    e "Voy... voy bien... solo tengo algo de ansiedad supongo."

    a "Normal que la tengas..."

    return

label cap2bad_evan2:
    scene bg salonclases2 with fade

    show evan ladobrazo2 at center with dissolve

    e "¿De vuelta de nuevo?"

    a "S...sí"

    "El chico carraspeó y luego soltó un suspiro."

    show evan ladobrazo with dissolve

    e "Como sea... Mataría por fumar en este momento."

    a "¿Fumas?"

    e "Sí, desde hace tiempo lo hago, ayuda a calmar mi ansiedad..."
    
    show evan gimmeceja with dissolve

    e "¿Tú no fumas?"

    a "Ah... no es que no fume, es solo que nunca lo he intentado, no me llama la atención del todo."

    show evan normal with dissolve

    e "Ya veo, una pena, sería increíble que trajeras algún encendedor."

    a "¿Calma tu ansiedad entonces?"

    show evan lado2 with dissolve

    e "Sí, bueno, mantiene mi mente ocupada, y, no lo sé, quizás es relajante."

    show evan lado with dissolve
    
    e "Mi psicóloga me explicó algo al respecto pero realmente no le presté atención."

    a "Tengo entendido que es un... estimulante."

    a "Ayuda a distraerte... bueno, eso es lo que me dijeron a mí... o, quizás lo leí en alguna parte."

    "Busqué entre mis bolsillos, luego en mi pequeña mochila sacando un encendedor."

    a "¿Este te sirve?"

    show evan feliz with dissolve

    e "Es perfecto."

    e "Lo haré fuera del salón, no me gustaría que los demás acaben mareados por el olor a tabaco."

    show evan pensando with dissolve

    e "¿Por qué traías uno? Si no eres... fumador."

    a "Oh... Suelo quemar las historias que no me agradan, así que, eso."
    
    show evan normal with dissolve

    e "Ok, supongo que es una incógnita que dejaré para después."

    a "¿Por qué comenzaste a fumar? Si puedo preguntar, claro."

    show evan ladobrazo with dissolve

    e "Mi padre y mi madre no eran muy saludables que digamos."

    show evan ladobrazo2 with dissolve

    e "Bueno, ellos fumaban y tomaban mucho, por ende terminé haciéndolo..."

    show evan pensando with dissolve

    e "Es curioso que haya acabado como biólogo sabiendo el daño que esto le causa a la vida."

    a "¿Y tomas?"

    show evan normal with dissolve

    e "No, bueno, no tanto... He evitado el alcohol... sobre todo por que manejo."

    show evan ceja with dissolve

    e "¿Tú? No te ves como el tipo de persona que sea un santo."

    a "Ah, ¿un santo? Para nada..."

    a "Estudio literatura así que... te podrás dar una idea de lo que ha pasado por mi interior."

    show evan lado with dissolve

    e "Eres una persona muy curiosa, Arden."

    a "¿L...Lo crees? Gracias... supongo."

    show evan feliz with dissolve

    e "Cuando salgamos, ¿qué te parece si salimos por unos tragos? Conozco un buen lugar."

    a "Sí, suena maravilloso..."

    hide evan with dissolve

    "Al acabar la conversación senti mi rostro sonreir, casi como un bobo enamorado."

    "Dios, debo controlarme, no es momento para pensar en estas cosas."

    return

label cap2bad_hanna:
    $ hasTalked_Hanna = True

    scene bg salonclases2 with fade

    show hanna llorar at center with dissolve

    "Me acerque a Hanna sabiendo que necesitaba compañia, sus ojos se llenaron de lagrimas al verme cayendo en llanto una vez más"

    h "¿Qué quieres?"

    "Me acerqué y me senté a su lado deslizándome un poco lejos para no hostigarla con contacto físico."

    a "Perdón... no pude hacer nada."

    show hanna miedohabla with dissolve

    h "Nadie... nadie podía hacer nada..."

    h "No puedo entender..."

    show hanna despair with dissolve

    h "No puedo entender cómo es que no pude hacer algo."

    "Ella se culpaba, era obvio."

    a "Lo lamento..."

    show hanna miedohabla with dissolve

    h "No era mala persona. Solo, hacia lo que creía que era mejor para todos, tenía miedo de perder a más gente."

    a "¿A qué te refieres?"

    h " Bueno... "
    
    h "Hay personas que intentan hacer lo correcto de forma equivocada, solo que... "

    show hanna normal with dissolve
    
    extend "ella se esforzaba mucho por mantener sus ideales y su vida recta, no tenía muchos amigos por eso."

    a "Ya veo... "
    
    extend "la verdad... "
    
    extend "no la conocía tan bien como tú."

    show hanna miedohabla with dissolve

    h "No... nadie la conocía..."
    
    h "Yo era su única amiga, era quien la juntaba con el resto, ¿sabes?"

    a "Y... ¿cómo la conociste tú?"

    show hanna explicando with dissolve

    h "Oh, eso fue hace mucho tiempo."

    show hanna normal with dissolve

    h "Nos conocimos en la escuela antes de la universidad, creo que yo era muy introvertida en ese entonces, no solía salir de mi recámara por días y tampoco tenía muchos amigos."
    
    h "Lo único que me gustaba era el deporte, en ese entonces estaba entrenando artes marciales."

    a "¿Artes marciales? Debes de ser una especie de ninja."

    show hanna sonrisa with dissolve

    h "Me gustaría serlo, quizás en el futuro."

    show hanna normal with dissolve

    h "Ella entró tarde a la escuela, era muy callada y los chicos de mi salón no querían conocerla, quizás porque era muy ruda y agresiva."

    h "A mí no me solían molestar por mi desempeño en el deporte."

    h "Así que... "

    show hanna emocionada with dissolve

    extend "un día, ella fue a verme a mi presentación, fue la única persona del salón que fue..."

    h "Se acercó a mí y me pidió ser su amiga... desde ahí hemos sido inseparables."

    a "Suena muy lindo."

    h "Lo es... "

    show hanna miedohabla with dissolve
    
    extend "Es una pena que nadie la comprendiera... deseaba que hiciera muchos más amigos."

    menu:
        "Quizás podríamos honrarla de alguna manera, ¿no lo crees?":
            a "Quizás podríamos honrarla de alguna manera, ¿no lo crees?"

            show hanna sonrisa with dissolve

            h "Sí... sí, supongo que sí..."

            show hanna miedohabla with dissolve

            h "No creo que ella hubiera deseado que me quedara lamentando su muerte... "
            
            show hanna emocionada with dissolve

            extend "hay que encontrar una forma de salir."

        "Ojalá hubiera podido ser su amigo.":
            a "Ojalá hubiera podido ser su amigo."

            show hanna emocionada with dissolve

            h "Estoy segura de que se hubieran llevado... muy bien ustedes dos."

        "Lamento mucho tu pérdida...":
            a "Lamento mucho tu pérdida..."

            show hanna sonrisa with dissolve

            h "Gracias... "

            show hanna normal with dissolve
            
            h "Deberíamos encontrar una forma de salir..."

    return

label cap2bad_felix:
    $ hasTalked_Felix = True

    scene bg salonclases2 with fade

    "Felix jugaba con una especie de pluma en su mano, quizás la traia en su bolso o algo parecido, miraba atentamente al techo con un tono juguetón."

    show felix sonrisa at center with dissolve

    f "Oh, Arden..."

    "Se veía bastante alegre a pesar de la situación."

    a "Recuerdas mi nombre..."

    show felix sonrisahabla with dissolve

    f "¡Claro! Katherine hablaba mucho sobre ti."

    a "¿Si?"

    show felix caderashabla with dissolve

    f "Sí, de hecho me parece genial poder hablar mas contigo."

    a "¿P-Por qué?"

    show felix pensando2 with dissolve

    f "Bueno, ahora si puedo conocerte en persona y no a base de algo que me dice alguien"
    
    show felix sonrisahabla with dissolve

    extend ", ¿me entiendes?"

    a "Sí, supongo que sí..."

    show felix normal with dissolve

    f "¿Por qué la cara larga?"

    a "Acaban de morir... dos personas... ¿cómo puedes estar tan... tranquilo?"

    show felix pensando with dissolve

    f "Bueno, es que no van a volver, ¿cierto? Tampoco podemos lamentarnos mucho tiempo..."

    a "Pero..."

    show felix normal with dissolve

    f "¿Pero?"

    a "¿No te sientes... mal?"

    f "Claro que me siento mal... "

    extend "Es solo que... "

    show felix manofrentepreocupado with dissolve

    extend "mi mente parece intentar bloquearlo..."

    show felix manofrentepreocupadohabla with dissolve

    f "No sé como explicarlo, es como una especie de mecanismo de defensa."

    a "Ah..."

    show felix sonrisahabla with dissolve

    f "Pero, es mejor no pensar en eso"
    
    show felix manofrentepreocupadohabla2

    f "La verdad es que... a pesar de todo, Katherine era una excelente chica."

    a "Sí... realmente lo era."

    show felix sonrisa with dissolve

    f "Ella debe estar orgullosa de ti, y de lo lejos que has llegado."

    a "¿En serio lo crees?"

    show felix sonrisahabla with dissolve

    f "Claro... conocía a Katherine mejor que nadie."

    a "Supongo que sí..."

    "Realmente no sé si el la conoce más o yo, es imposible decir con certeza."

    return
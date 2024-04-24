label cap4true_evan:
    $ evan_counter += 1

    $ evan_cap4_talk = True

    #bg oficina

    scene bg oficina with Fade(0.3, 0.1, 0.3)

    #show evan

    show evan nmcigarlado at center with dissolve

    "Evan se encontraba en el marco de la puerta con un cigarro en la boca viendo hacia otro lado."

    "Cuando pude acercarme, pude ver una horrible cicatriz sobre su rostro."

    show evan nmnormal with dissolve

    "Al verme, Evan ocultó el cigarro y se encogió de hombros."

    e "Perdón, no te escuché llegar."

    a "N...No te preocupes ¿Estás bien?"

    show evan nmnormalhabla with dissolve

    e "Solo un poco estresado, siento que vamos en círculos y no encontramos nada."

    a "Sí, creo que yo también siento lo mismo..."

    "Hubo un pequeño silencio antes de que pudiese decir algo."

    a "¿Puedo... preguntar?"
    
    show evan nmcejahabla with dissolve

    e "No es muy agradable..."

    a "Ah...perdón, no quería molestar."

    show evan nmnormal with dissolve

    e "¡No! "
    
    extend "Ah"
    
    extend ", digo"
    
    extend ", no molestas."

    e "Es complicado hablar de esto... pero no es que pueda ocultarlo para toda mi vida."

    play music "audio/repentance.mp3" volume 0.25

    show evan nmcigarhabla with dissolve

    "Sacó nuevamente su cigarro antes de continuar."

    e "Mis padres no me querían del todo, si no fuera por las leyes del país quizás yo no existiría, y añádele el odio que le tendrían los familiares..."

    show evan nmcigarladohabla with dissolve

    e "Soy un niño no deseado, un niño no deseado de una familia adinerada, además de que nacer enfermo me hizo... ser mucho menos deseado, en serio no sé cómo es que sigo vivo."

    e "Esto..."

    "Evan apuntó a su rostro y bajo el cubrebocas para enseñar su cicatriz."

    e "Lo hizo mi madre, suena a un cliché de película... y no suele pasar a la gente adinerada..."

    a "Suena horrible..."

    show evan nmcigarladohabla2 with dissolve

    e "Lo fue..."

    e "Ocurrió cuando tenía 17 años más o menos... el gobierno me separó por abuso familiar pero... "
    
    extend "bueno"
    
    extend ", ¿qué diría el resto de la familia...?"

    show evan nmcigarnormal with dissolve

    e "Así que, con un par de sobornos y una buena cantidad de dinero me hicieron regresar a casa sin que nadie se enterara."

    a "Lo lamento mucho."

    show evan nmcigarhabla with dissolve

    e "Nada que lamentar."
    
    e "La gente con dinero es así... "

    extend "solo mueven las cosas cuando les conviene y cuando lo necesitan."

    "Se encogió de hombros nuevamente."

    a "Sí, supongo que sí... solo, no sabía... bueno..."

    show evan nmcigarlado with dissolve

    e "Hay muchas cosas que se quedan en las penumbras..."

    show evan nmcigarladohabla2 with dissolve

    e "Como sea, ahora mi propósito es robarles lo más que pueda de dinero, quizás así al menos pueda sacar algo de provecho."

    e "Lo bueno es que estoy estudiando lejos de casa y solo me mandan el dinero, puedo hacer lo que quiera."

    a "Eso es bueno..."

    show evan nmcigarladosonrisa with dissolve

    e "Sí, es lo mejor que me ha pasado"

    show evan nmcigarladohabla2 with dissolve
    
    e "¿Qué me dices de ti?"

    a "¿Yo? "
    
    extend "Oh"
    
    extend ", mi vida es muy aburrida, no creo poder decirte algo interesante la verdad."

    a "Bueno, mis padres son escritores, yo también..."

    a "Ammm, supongo que la barra está muy alta para mí... "
    
    extend "todos esperan que sea como ellos o quizás mejor..."

    show evan nmcigarhabla with dissolve

    e "Tsk, la sociedad haciendo de las suyas."

    a " Sí, supongo que sí... "
    
    extend "solo espero poder cumplir sus expectativas."

    show evan nmcigarladohabla with dissolve

    e "¿Quieres mi consejo?"

    e "No lo intentes, solo vivirás para los demás y nunca para ti mismo..."

    a "Yo... Lo tendré en cuenta... gracias..."

    stop music fadeout 0.5

    return

label cap4true_freya:
    $ freya_counter += 1

    #bg oficina

    scene bg oficina2 with Fade(0.3, 0.1, 0.3)

    play music "audio/repentance.mp3" volume 0.25

    #show freya

    show freya normal at center with dissolve

    "Freya observaba las estanterías y movía los libros en alguna especie de orden, sus ojos rojos aún concentrados fijamente en lo que ocurría si los movía."

    a "Hey."

    show freya normalhabla with dissolve

    fr "Oh, Arden."

    a "Sí, ese soy yo... ¿qué haces?"

    show freya apunta2 with dissolve

    fr "Oh, solo estoy moviendo los libros en caso de que algún pasadizo se abra, o alguna pista caiga milagrosamente..."

    a "Se ve que te estás esforzando."

    show freya normalhabla with dissolve

    fr "Claro... bueno, eso intento..."

    show freya normal with dissolve

    fr "La verdad creo que hemos salido vivos muchas veces de formas milagrosas..."

    a "Si, tienes razón..."
    
    extend " como si alguien... nos hubiese dejado las cosas para salir con vida, ¿no lo crees?"

    show freya ladohabla2 with dissolve

    fr "Sí, bueno, si milagrosamente alguien nos esta ayudando quiero creer que... nos quieren salvar o algo."

    a "Es como si el espiritu de Hanna aún te estuviese ayudando."

    show freya sonrisa with dissolve

    fr "Sí, como si... realmente me estuviese ayudando..."

    fr "Hey... "
    
    extend "cuando salgamos... "
    
    extend "si es que salimos... "
    
    extend "deberíamos salir a algun lado."

    a "Pensé que me odiabas..."

    show freya pensarhabla with dissolve

    fr "Quizas eres un poco molesto, y... demasiado... "

    extend "como decirlo... "

    show freya normal with dissolve
    
    extend "inseguro."

    show freya sonrisahabla with dissolve

    fr "Pero eso no quita que... seas una buena persona."

    a "Gracias Freya..."

    a "Bueno, me gustaria salir contigo a algun lado si salimos de esta."

    show freya caderassonrisa with dissolve

    fr "Excelente... "

    show freya sonrisa with dissolve
    
    extend "seguiré buscado por acá."

    a "Sí, yo también."

    stop music fadeout 0.5
    
    return

label cap4true_felix:
    #bg oficina

    scene bg oficina2 with Fade(0.3, 0.1, 0.3)

    play music "audio/downtime.mp3" volume 0.25

    "Me acerqué a Felix quien tenía un libro entre sus manos, uno pequeño, pero eso no evitó que lo cerrase con fuerza al momento."

    #show felix

    show felix sonrisahabla at center with dissolve

    f "Oh, eres tú."

    a "¿Quién creías que era?"

    show felix manofrentepreocupado with dissolve

    f "Evan..."

    a "No parece agradarte, en ese caso."

    show felix normal with dissolve

    f "No es eso... bueno... tal vez un poco, es una persona muy seria y me aterra."

    a "¿Te aterra? Esa es una palabra un poco grave."

    show felix manofrentepreocupadohabla2 with dissolve

    f "Sí, supongo que sí, pero creo que es esa mirada, y... bueno, no sé, las personas poco sociables me suelen dar desconfianza."

    a "¿Cómo lo conociste?"

    show felix normal with dissolve

    f "¿A Evan?"

    show felix dedohabla with dissolve

    f "Katherine nos presentó hace mucho tiempo, pero fue una presentación únicamente formal... fuera de eso no hablamos mucho, Katherine era la que hacía todas las conversaciones."

    a "Ya veo... Bueno, no creo que sea mala persona..."

    show felix pensando2 with dissolve

    f "No, supongo que no..."

    a "¿Y cómo te sients?"

    show felix manofrenteceja with dissolve

    f "¿De qué? Estoy bien."

    a "De tu pie... te lo habías torcido, ¿no? Espero no te hayas hecho más daño mientras corríamos de un lado al otro."

    "Temí recordárselo, parecía que se le había olvidado."

    "Felix se veía desconcertado por la pregunta, como si no supiese de qué le estaba hablando."

    show felix normal with dissolve

    f "Mi..."
    
    extend "pie... "

    show felix sonrisahabla with vpunch
    
    extend "¡OH, OH! ¡Sí! "
    
    extend "No, no duele para nada, quizás solo fue cosa del momento pero está perfecto."

    a "Oh, ya veo."

    a "Bueno, eso es genial."

    a "Si en algún momento te cansas seria bueno que te sientes un rato, con eso de que la enfermería está cerrada no sé si sea bueno que sigas corriendo si estás lastimado."

    show felix caderashabla with dissolve

    f "¡Estoy bien, no te preocupes!"

    "Felix rió una vez más tomando un libro de la estantería."

    show felix pensando with dissolve

    f "Será mejor que continúe buscando, no me gustaría perderme nada. Después de todo, ustedes son los que han encontrado todas las pistas..."
    
    show felix manofrentepreocupado with dissolve

    f "Oh... "
    
    extend "me siento patético..."

    a "Oh, no te preocupes por eso, fueron mayormente casualidad y quizás mucha suerte."

    show felix pensando with dissolve

    f "Sí, bueno, es que eso de no saber de cultura me deja un poco atrás."

    a "Nada que no se pueda aprender."

    show felix pensando2 with dissolve

    f "Sí... tienes razón..."

    stop music fadeout 0.5

    return
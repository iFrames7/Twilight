label cap2true_evan:
    $ evan_counter += 1

    #bg bibliotecatwilight

    scene bg black with Fade(0.3, 0.1, 0.3)

    "No confiaba en Evan, de hecho, era la última persona con la que iría, pero, teniendo en cuenta que no confío en él, tal vez es la mejor razón para seguirlo."

    #show evan

    show evan espalda at center with dissolve

    "Mi cuerpo se movió lentamente hasta donde Evan estaba, se veía molesto, pues tenía su ceño fruncido, pero sus manos se movían con rapidez mientras examinaba los libros."

    a "Hey."

    show evan defensivo with vpunch

    e "¡MIERDA!"

    "Evan tiro el libro que tenia en sus manos, parece que mi presencia lo asusto realmente, el chico solo volteo a verme fulminando con la mirada."

    show evan ceja with dissolve

    e "Creí haber dicho que vendría solo..."

    menu:
        "No puedo confiar en dejarte solo...":
            a "No puedo confiar en dejarte solo..."

            "Evan chasqueo con la lengua al escucharme, quizas mi respuesta fue un poco agresiva, solo volteo los ojos molesto y suspiro."

            show evan ladobrazo with dissolve

            e "Bien, pero no hagas mucho ruido."

            "¿De que habla? Si el que gritó fue él."

        "Creí que podía acompañarte un rato.":
            a "Creí que podía acompañarte un rato."
            
            show evan ladobrazoenojado with dissolve

            e "No necesito compañía, ¿acaso no entiendes?"

            a "Perdona... Es solo que... no me gustaría que estes solo después de lo que pasó."

            e "¿Realmente no sabes entender verdad?"

            show evan lado2 with dissolve

            "Evan me observó por un momento más, su mirada se enterneció y soltó un suspiro."

            show evan normal with dissolve

            e "Bien... puedes quedarte, solo... no hagas mucho ruido."

        "Lo lamento, puedo irme si quieres.":
            a "Lo lamento, puedo irme si quieres."

            show evan despair

            "Evan enterneció la mirada, o al menos eso parecía, como si se hubiese arrepentido de lo que dijo."

            show evan normal with dissolve

            e "No, está bien... solo no hagas ruido, ¿sí?"

            "Seguido de esto, se volteó para seguir buscando en sus libros."

    #hide evan

    hide evan with dissolve

    "Al igual que él, me voltee para poder seguir viendo los libros, página por página, aunque claro, Evan era mucho más rápido que yo, como si leyese dos líneas y entendiese lo que decía el libro por completo."

    "O quizas solo estaba abriendolos y cerrandolos al ver que tenian simbolos indescriptibles."

    #bg bibliotecatwilight (con un fade para simular que pasó tiempo)

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Nada, no parecía haber nada entre la pila de libros que habían, pero mis ojos quizás no estaban centrados al cien porciento en los libros, si no en Evan."

    a "Ah... ¿encontraste algo?"

    #show evan

    show evan pensando at center with dissolve

    e "No, solo símbolos y cosas que no puedo comprender, parece que realmente no hay nada aquí..."

    a "Entonces... solo perdimos el tiempo..."

    show evan normal with dissolve

    e "No creo que sea el caso..."

    e "A veces solo tenemos que confirmar cosas que parecen obvias."

    show evan gimme with dissolve

    e "Quien sabe, si no hubieramos regresado tal vez la duda seguiría en tu cabeza, ¿no lo crees?"

    a "Sí... supongo que sí, aun así, perdimos mucho tiempo, ¿no?"

    show evan lado with dissolve

    e "No podemos lamentarnos constantemente cuando perdemos el tiempo, estaríamos perdiendo más tiempo haciendolo."

    a "S...sí... supongo que sí."

    show evan normal with dissolve

    e "No soy la mejor persona para dar consejos pero... ten algo de confianza."

    e "Si sigues así solo lamentarás tus decisiones y nunca aprenderas de ellas."

    a "S...supongo que sí."

    "¡¿Cuándo se volvió esto una plática motivacional?!"

    "Solo queria saber si habia encontrado algo..."

    "Aun así, las palabras de Evan hacen que mi corazón se caliente un poco."

    "¿Lo estoy juzgando demasiado?"

    show evan ladobrazo with dissolve

    e "Deberíamos seguir buscando..."

    a "Sí, tienes razón..."
    
    return

label cap2true_freya:
    $ freya_counter += 1

    #bg bibliotecatwilight

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Claro que la chica se veía molesta, ¿tal vez deberia ir a disculparme?"

    "¿Por qué? ¿Por qué no elegimos su opción?"

    "Bueno, quizás podría hablar de eso, ¿no?"

    "Caminé hasta Freya quien examinaba detrás de la mesa de informes en la biblioteca."

    a "Hola..."

    #show freya

    show freya normalhabla at center with dissolve

    fr "Oh, eres tú, chico de las decisiones."

    a "¿Estás... molesta?"

    show freya ladohabla2 with dissolve

    fr "No."

    "Su tono obviamente decía lo contrario, sonaba a una especie de niño enojado porque no le dieron el juguete que quería en navidad o algo así."

    a "Entonces..."

    show freya apunta with dissolve

    fr "¿No tienes a nadie más a quien molestar?"

    menu:
        "No quiero molestar, solo queria ver si necesitabas ayuda.":
            a "No quiero molestar, solo queria ver si necesitabas ayuda."

            show freya ladohabla2 with dissolve

            fr "Bueno, entonces ponte a hacer algo de provecho y no hagas preguntas ridículas, solo vamos a perder el tiempo así."

            show freya normalhabla with dissolve

            fr "Ayúdame con los estantes de en frente."

        "Fuiste la primera persona con quien me tope...":
            a "Fuiste la primera persona con quien me tope..."

            show freya caderaspreocupada with dissolve

            fr "Vaya suerte, supongo que por eso estás aquí sin hacer nada..."

            "Tenía un tono molesto en su forma de hablar, se quedo viéndome un par de segundos antes de soltar un suspiro."

            show freya normalhabla with dissolve

            fr "¿Que tal si me ayudas a buscar en en esos estantes ya que estás aquí?"

        "(Guardar silencio)":
            "No supe qué responder, para ser honestos su tono era bastante amenazante por lo cual solo me separé un poco de la mesa guardando silencio."

            show freya normalhabla with dissolve

            "Freya notó esto y se acomodó las gafas antes de hablar."

            fr "Bueno, ya que estás aquí supongo que puedes ayudarme a buscar entre los estantes frente a ti."

    #hide freya

    hide freya with dissolve

    "Asintiendo con la cabeza caminé hacia el estante mencionado buscando entre las revistas que se encontraban ahí, solo habían ilustraciones y parecían ser una especie de simbolos o... runas, realmente no las comprendía."

    "Aparté aquellas que parecían ser importantes y dejé de lado aquellas que definitivamente no entendía luego voltee a Freya quien parecía ya estar echándole un vistazo a las revistas que yo había entregado."

    #show freya

    show freya normal at center with dissolve

    a "¿Encontraste algo?"

    fr "Solo runas... símbolos, nada que no sepamos."

    "Sus ojos se fulminaron ligeramente a la revista y me acerqué para poder ver lo que hacía de forma curiosa."

    show freya pensarhabla with dissolve

    fr "Conozco este símbolo, solo, no recuerdo qué es..."

    "Era un símbolo nórdico, o una runa nórdica más bien, también recordaba haberla visto en algun libro."

    show freya normalhabla with dissolve

    fr "Seria maravilloso tener señal o algo parecido para buscar..."

    a "Podríamos tomarle una foto y buscarlo después."

    show freya caderassonrisa with dissolve

    fr "¿Cuando ya estemos muertos? HAH."

    "Ella bufó en alto haciendo que solo me alejase un poco, su rostro se vio confundido y pareció querer cambiar su error con un carraspeo."

    show freya angustiada with dissolve

    fr "No, puedo llevarlo y en caso de necesitarlo lo tendre cerca."

    "La chica rasgó la pagina de la revista que contenía el simbolo y luego la guardó en su bolsillo del pantalón."

    show freya normalhabla with dissolve

    fr "Sigamos buscando, tal vez encontramos algo más por aquí..."

    return

label cap2true_hanna:
    $ talk_hanna = True

    #bg bibliotecatwilight

    scene bg black with Fade(0.3, 0.1, 0.3)

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

    show hanna normal with dissolve

    h "Mira."

    "Hanna tomó un libro el cual parecía encriptado en muchos símbolos, aunque no pude ver nada especial fuera de lo que ya había visto."

    a "¿Qué tiene?"

    show hanna explicando with dissolve

    h "Este símbolo, lo vi en uno de los posters de la cafetería."

    "Ella apuntó el símbolo, abrió el libro y la primera página era una imagen del monstruo."

    show hanna llorar with dissolve

    "Hanna, aterrada, soltó el libro y se cubrió la boca nerviosa, mi cuerpo también se asustó y se movió hacia atrás por el mismo miedo que llenó a Hanna."

    show hanna miedohabla with dissolve

    h "P...perdón."

    "La chica se agachó para tomar el libro."

    a "N...No te preocupes, yo también me asusté."

    "Intenté calmarla a pesar de que mi corazón también latía con mucha fuerza."

    a "¿Q...qué dice?"

    "Hanna abrió el libro una vez más y hojeó las letras."

    show hanna explicando with dissolve

    h "No comprendo mucho... pero, quizás haya una clase de diccionario cerca de aquí. Segiré buscando, puede que encuentre algo de valor."

    "Los ojos de la chica se iluminaron por la emoción, no era una mala idea, de hecho aquella esperanza llenó mi corazón de emoción."

    a "Sí, tienes razón, yo seguiré buscando de otro lado."

    return

label cap2true_felix:
    #bg bibliotecatwilight

    scene bg black with Fade(0.3, 0.1, 0.3)

    #show felix

    show felix pensando at center with dissolve

    "Felix se quedó en el centro de la habitación, caminaba casi que en círculos viendo las estanterias y las mesas que estaban ahí para estudiar, sus ojos puestos casi en un vacío que no podia comprender."

    a "Hey..."

    show felix sonrisahabla with dissolve

    f "¡Oh! Arden."

    "Volteo a verme ladeando la cabeza ligeramente."

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

    "Sería poco usual, pero tendría sentido, este lugar está alterado... De repente sentí una respiración detrás de mí, o una presencia, mi cuerpo se tensó y lentamente voltee hacia atrás."

    #show felix

    show felix sonrisahabla at center with dissolve:
        zoom 3 yalign 0.3
    f "¿Encontrasate algo?"

    a "N...No..."

    show felix pensandoceja with dissolve

    f "Quizás no hay nada por aquí después de todo... bueno, será mejor buscar en otro lado, no hay que perder el tiempo aquí."

    a "Sí, tienes razón."

    return
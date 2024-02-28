label cap3true:
    $ codigo_real = 7648

    #bg dream2 ?

    scene bg black with Fade(1.0, 1.0, 1.0)

    "Nuevamente, estoy en este vacío..."

    "Pero puedo ver a más personas... "

    extend "personas a la lejanía que no distingo."

    "Mi cuerpo se levanta ahora caminando hacia ellos pero por más que camino no logro acortar la distancia que tengo con ellos."

    menu:
        "¡¿Quiénes son?!":
            a "¡¿Quiénes son?!"

        "¡¿Dónde están?!":
            a "¡¿Dónde están?!"

        "¡AYUDA!":
            a "¡AYUDA!"

    "Aquellas siluetas voltean a mí, ojos blancos por completo, mi cuerpo se siente nervioso."

    a "¡Díganme algo!"

    "{color=#ffffff}???{/color}" "𒈓𒈙꧅𒈙𒈙"

    "Son palabras que no puedo distinguir, un lenguaje extraño que ya había escuchado en el pasado."

    #bg salonclases

    scene bg black with Fade(1.0, 1.0, 1.0)

    "Abrí mis ojos lentamente acostumbrándome la luz, puedo escuchar las voces de mis compañeros a la lejanía como pequeños ecos."

    "Pronto las memorias regresan: "

    extend "cuando salimos de la biblioteca mi cuerpo se paralizó una vez más, Felix tomó la gorra de mi sudadera y me arrastró lejos hasta llegar al salón."

    "Sí, me acordaba de lo que había ocurrido, como mi cuerpo había dejado de reaccionar por el miedo al igual que a Freya gritando que Evan la soltase."

    #show freya

    fr "¡IDIOTA!"

    "Se escuchó el fuerte grito de Freya dándole una fuerte cachetada a Evan. Éste inmediatamente caminó hacia atrás y se sostuvo con una mesa comenzando a toser."

    fr "¡CÓMO TE ATREVES! ¡PODÍA SALVARLA! ¡PODÍA... PODÍA RESCATARLA!"

    #show evan nomask

    "El cubrebocas de Evan cayó revelando una horrible cicatriz a lo largo de su boca, se veía vieja, quizás tenía ya mucho tiempo."

    "Alrededor de su mismo rostro tenía varias cicatrices pero ninguna era tan grande como esta, como si un animal lo hubiese atacado antes."

    "Evan apartó la vista para comenzar a toser, sangre salía de su boca mientras éste tosía."

    e "Ibas a morir también..."

    fr "¡LO HUBIERA PREFERIDO!"

    "Freya lo tomó de la chaqueta con fuerza aunque después se detuvo, quizás fue el rostro herido del chico o la facilidad con la que aquella pudo tomar su cuerpo."

    #hide evan ?

    "Molesta, únicamente le dio un empujón y fue suficiente para que Evan se tambaleara y cayera entre las mesas."

    "Rápidamente me levanté, reaccionando inmediatamente, mi cuerpo se movió hacia Evan para ayudarlo a levantarse."

    fr "Tú... Tú tienes la culpa de todo."

    "Esta vez me estaba apuntando a mí, sus ojos furiosos viéndome con determinación."

    a "¿Y-... yo?"

    fr "Sí, no debimos ir a la biblioteca, yo sabía que iba a ser un error."

    fr "¡¿Y qué fue lo que lograste?! "
    
    #cambia expresion

    extend "¡NADA!"

    "Su cuerpo se movió hacia mí, su puño cerrado hasta alzarse con la intención de golpearme pero se detuvo antes de llegar."

    fr "¡Ustedes, son unos idiotas! Mataron a mi amiga, ustedes... ustedes dejaron que muriera..."

    #hide freya

    "La chica se dio la vuelta dándole un fuerte empujón a una mesa conteniendo sus lágrimas moviéndose a una esquina del salón."

    #show evan

    a "¿Estás bien?"

    "Esta vez voltee a ver a Evan."

    e "Sí..."

    "Sabía que mentía, pero tampoco quise presionarlo."

    "Mis manos buscaron entre mis bolsillos algo que pudiera usar para cubrirse."

    e "Déjalo así..."

    menu:
        "Estás herido, necesitas ayuda":
            a "Estás herido, necesitas ayuda."

        "Pero quiero ayudar":
            a "Pero quiero ayudar."
        
        "No puedo dejarlo así":
            a "No puedo dejarlo así."

    e "Estoy bien..."

    "Un poco asustado asentí con la cabeza dándome la vuelta, no sin antes recibir un pequeño \"gracias\" de la boca de Evan."

    #hide evan

    #show felix

    "Caminé a Felix el cual sostenía los libros entre sus manos."

    f "Fue-... Fueron los que pude agarrar, el último se quedó en la biblioteca."

    "Felix los extendió para ofrecerlos."

    "Los examiné lentamente, algo se sentía raro. No sé qué era, pero era algo raro."

    if talk_hanna:
        "El libro era distinto, este era uno que Hanna me había enseñado cuando platicamos."
        
        "La portada era la misma pero al momento de abrirlo el contenido cambiaba, ya no estaba la imagen del monstruo en ninguna de las páginas y tampoco los símbolos que antes había visto."

        "¿Quizás los libros cambiaban su contenido después de un tiempo?"
    else:
        "Por más que los observaba una vibra muy extraña salía de los libros, se sentían oscuros, causaban que un escalofrío recorriera por mi espalda baja por la sensación."

    f "¿Descubriste algo?"

    a "No, nada, no entiendo ninguna palabra."

    f "Bueno, era de esperarse, todos los libros dentro de la biblioteca estaban así, dudo mucho que Hanna haya encontrado algo de valor."

    "Tragué frío, la saliva de mi boca se deslizó como hielo por mi garganta causando nerviosismo en mi interior se intensificara por las palabras de Felix."

    a "No creo que sea así."

    "Intenté mentirme a mí mismo..."

    "¿Y si realmente Hanna no había encontrado algo? "
    
    extend "¿Acaso su muerte había sido en vano?"

    "No"
    
    extend ", no tenía sentido."

    "Mis ojos pasaron por las páginas de los libros "
    
    extend "¿alguna señal? "
    
    extend "¿Hay algo que Hanna haya dejado?"
    
    "Nada, absolutamente nada."

    "Sentí como se llenaban de lágrimas por la impotencia, no quería asumir que su muerte había sido para nada."

    f "Bueno, si no son de utilidad deberíamos dejarlos, solo nos estorbaran si tenemos que correr."

    a "Sí... supongo que tienes razón."

    #hide felix

    #bg salon clases

    label cap3true_sideselection:
        scene bg black with Dissolve(1.0)

        "Dejando los libros de lado, no sin antes darles una última ojeada, un suspiro salió de mi interior."

        "El salón se quedó completamente en silencio a salvo de un par de tosidos de parte de Evan el cual ya traía su cubrebocas puesto nuevamente."

        "Felix estaba recostado sobre la puerta viendo de vez en cuando por la ventana para comprobar que el monstruo no viniese."

        "Freya estaba del otro lado de la habitación de brazos cruzados viendo a algún punto vacío de la habitación."

        $ freya_cap3_talk = False

        menu:
            "Cuidar de Evan":
                call cap3true_evan from _call_cap3true_evan

            "Hablar con Freya":
                call cap3true_freya from _call_cap3true_freya

            "Acompañar a Felix":
                call cap3true_felix from _call_cap3true_felix

    #bg salonclases

    scene bg black with Fade(0.3, 0.1, 0.3)

    #show evan

    #show freya

    #show felix

    "Caminé al centro de la habitación, los demás parecieron juntarse intuitivamente."

    "¿Acaso me había convertido en una especie de líder?"

    "No quería eso, suelo tomar pésimas decisiones, no deberían de estarme siguiendo en absoluto."

    e "¿Y ahora qué?"

    "Evan preguntó, Freya pareció ignorarlo."

    a "Amm, bueno, la verdad no lo sé."

    "Mi esperanza era lo que estaba en la biblioteca pero solo había acabado con un par de libros inútiles y una ilustración de Loki."

    fr "Quizás podríamos ir a la oficina del director, es otra biblioteca ahí dentro."

    e "Pero eso está en el segundo piso."

    fr "Puedes quedarte aquí si quieres."
    
    a "No, hay que permanecer unidos."

    f "¿Y eso a que nos ha llevado? Quizás deberíamos separarnos."

    if freya_cap3_talk:
        fr "No, estoy de acuerdo con Arden."

        fr "Es más probable que podamos ayudarnos a escapar estando juntos que si nos separamos. "
        
        extend "Además, como ya había dicho, ninguna película de terror acaba bien si nos separamos."
    else:
        fr "No, estoy de acuerdo con..."

        "Hizo una pausa y volteo una vez más hacia Arden, aunque esta vez lo miraba pidiendo perdón."

        a "Arden."

        fr "Arden."
        
        fr "Es más probable que podamos ayudarnos a escapar estando juntos que si nos separamos. "
        
        extend "Además, como ya había dicho, ninguna película de terror acaba bien si nos separamos."

    "Tomando esto en cuenta quizás esa era la razón por la cual Hanna murió, se separó del grupo. Era más seguro ir unidos."

    e "Tsk, no iré."

    "Evan declaró dándose la vuelta y caminando a la entrada."

    a "¿A dónde vas?"

    e "No lo sé, lejos."

    #hide evan

    "Evan salió del salón sin decir nada más."

    "Mis ojos voltearon a  Freya quien se encogió de hombros como si no le importase del todo Evan, aunque, no pudo disimular que dio un paso para seguirlo."

    f "Bueno, entonces... ¿a la oficina del rector?"

    "Freya y yo asentimos con la cabeza"
    
    "Fue cuando Evan volviera a entrar cerrando la puerta del salón"

    #show evan

    extend ", sus ojos palpitaban terror y se notaba preocupado."

    e "Estamos jodidos."

    "Evan comenzó a toser, se llevó su antebrazo a su boca para cubrirse."

    fr "¿Qué?"

    e "¡¡Estamos jodidos!!"

    a "¿A qué te refieres?"

    e "Afuera, hay un humo, es tóxico. Lo conozco, tiene propiedades que investigamos una vez en clase."

    fr "Tsk, ¿cómo sabemos que no nos engañas?"

    e "¡¿POR QUÉ LOS ENGAÑARÍA?!"

    fr "¡Porque literalmente hace unos minutos no querías nada que ver con nosotros!"

    e "Claro, no es como que quiera volver a verte."

    fr "¿Huh? ¿Eso qué tiene que ver?"

    "Freya se acercó a él quitándolo de la puerta de un tirón. Ésta vio el humo desde la ventanilla de la puerta y luego se volteó a Evan de forma incrédula."

    e "Adelante, no pienso detenerte."

    #hide freya

    "La chica salió rápidamente cerrando la puerta detrás de ella"
    
    #show freya

    extend ", luego de unos segundos regresó."

    fr "Mierda... Estamos atrapados."

    a "¿A...atrapados?"

    fr "Las puertas del pasillo también están cerradas... no podemos salir de aquí... ¿En cuánto tiempo hace efecto el humo?"

    e "Quizás en ustedes unos 7 minutos para perder la conciencia, bueno, en el hipotético caso de que el salón esté lleno del humo, mientras tengamos oxígeno tenemos más tiempo."

    e "Yo, sin embargo, en 2 minutos estoy muerto..."

    fr "¡CALLA! ¡No dejaré que nadie más muera, ni siquiera tú! Hay que checar las rutas de evacuación."

    #maybe un bg que tenga el salon con humo, o un overlay de humo.

    "El humo comenzó a meterse lentamente debajo de la puerta cubriendo un poco los pies de todos."

    fr "¡Mierda, mierda!"

    f "La ruta de escape está bloqueada, Freya."

    fr "¡Debe de haber algo, alguna forma!"

    "La ansiedad ahora me empezaba a consumir: "
    
    extend "vas a morir, vas a morir, todos aquí van a morir."

    a "¡No quiero, no quiero, no quiero!"

    a "¡¡NO QUIERO MORIR!!"

    "Comencé a caminar hacia la salida desesperado y golpeé las ventanas con fuerza buscando romperlas."

    fr "¡ESPERA, NO! ¡Vas a alertar al monstruo!"

    a "Me voy a morir de todas formas."
    
    #un vpunch o algo chido, idk

    extend " ¡NOS VAMOS A MORIR FREYA!"

    fr "Tranquilo, vamos a encontrar la salida."

    fr "Hay que encontrar la salida."

    #hide evan, felix

    "Los otros dos asintieron con la cabeza y comenzaron a buscar entre los casilleros y cajones algo de utilidad."

    #hide freya

    "Sea lo que sea que dijeran, yo ya no los estaba escuchando"
    
    extend ", no"
    
    extend ", mis pensamientos estaban destrozados"
    
    extend ", tengo miedo"
    
    extend ", mucho miedo."

    "Mi cuerpo se deslizó sobre la pared hasta quedar en el suelo, el humo pesado invadiendo poco a poco mis pulmones mientras el pánico estaba llenándome."

    "No quiero morir"
    
    extend ", no quiero morir"
    
    extend ", por favor, no quiero morir." 
    
    "Era lo único que se repetía varias veces en mi cabeza."
    
    "No quiero morir, no quiero morir."

    "Mi desesperación aumentaba mientras las lágrimas caían recorriendo mis mejillas."
    
    "...Por favor..."
    
    extend "alguien, sálveme, por favor."

    menu:
        "Darse por vencido.":
            jump cap3true_badend1

        "No darse por vencido.":
            "{color=#435f21}???{/color}" "No te rindas"

    a "¿Katherine?"

    "{color=#435f21}???{/color}" "Yo sé, yo sé que tú eres mejor que esto."

    a "¡KATHERINE!"

    #vpunch probs

    "Alcé la cabeza rápidamente golpeándome contra la mesa y como si fuese un milagro un sobre cayó sobre mis piernas."

    "Estaba debajo de una mesa después de todo y el movimiento pareció haber despegado el sobre que estaba atado a la misma."

    "Tomé el sobre y lo abrí"
    
    #bg pista binario
    
    extend ", era un código, un código binario, y hasta abajo un C3."

    #bg salon con humoa

    #vpunch

    a "¡¡AHH!!"

    "Me levante con rapidez, golpeando mi cabeza."

    #show freya

    #show evan

    fr "HEY."

    e "¡Arden!"

    "Ambos estaban cerca, parecía que estaban gritando desde antes o quizás discutiendo como es de costumbre."

    a "¡Encontré algo!"

    #show felix

    f "¿Qué es?"

    a "Un sobre... debe traer algo que nos ayude, ¿no?"

    e "Código binario. "
    
    extend "¿Alguien aquí sabe leer... código binario?"

    "Todos negamos con la cabeza."

    a "Ah, estudie un poco, por... Historia de la literatura. Pero, no recuerdo todos los números..."

    "Tomando una pluma de mi bolsillo, anoté los números que conocía en la parte de atrás del sobre."

    a "Tendremos que adivinar el resto..."

    e "Es de cuatro números... aun así, ¿dónde se pone el código?"

    fr "¿En el C3? Es un casillero, ¿no?"

    "Freya volteó a los casilleros donde estaban ordenados por letras, y solo uno estaba cerrado."

    "Todos nos acercamos, habían varios números tachados a su alrededor y un par de puntos más."

    $ binario_fail_counter = 0

    label cap3true_binario:
        if binario_fail_counter > 3:
            jump cap3true_binario_fail

        $ codigo_input = int(renpy.input("Introduce el código:", 0000, allow="0123456789", length=4))

        if codigo_input != codigo_real:
            fr "No tenemos mucho tiempo, Arden. Concéntrate por favor."

            $ binario_fail_counter += 1

            jump cap3true_binario

    #bg salonclases humo

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Finalmente se abrió la puerta y ahí había otra ilustración doblada."

    a "Otra imagen..."

    "La desdoble para ver lo que tenía dentro. "
    
    #bg pistaolimpo

    scene bg black with Fade(0.3, 0.1, 0.3)
    
    extend "Era una imagen de una entrada, un cuadrado y líneas de perspectiva."

    a "Huh..."

    fr "La... Es la entrada del Olimpo."

    a "¿Perspectiva?"

    #bg salon de clases humo

    scene bg black with Fade(0.3, 0.1, 0.3)

    #show evan, freya, felix

    "Ladee mi cabeza confundido y Evan se encogió de hombros de la misma forma."

    a "Quizás si lo alineamos..."

    #bg salonalineado

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Poniéndolo en varias posiciones alrededor de la habitación, finalmente lo alineó con el pizarrón, revelando que la entrada del olimpo quedaba en un cuadro del techo."

    a "Hey... esa pieza..."

    #show freya

    fr "No perdemos nada, ¡rápido!"

    #hide freya

    "Ella corrió hacia la pieza del techo que apuntaba el olimpo y subiendo a una mesa la removió revelando así un pasadizo entre las ventilaciones, uno lo suficientemente amplio para que todos pudieran pasar."

    #show evan

    e "¡¿QUÉ ESPERAS?! ¡HAY QUE IRNOS!"

    "Freya asintió con la cabeza y todos comenzamos a subir ayudándonos entre nosotros."

    #bg ventilaciones ?

    "Ya dentro se escucha cómo el viento sopla con fuerza y recorre aquel lugar frío para mantener ventilados los salones."

    "Entre vueltas y el continuo miedo de la oscuridad, una pequeña luz se empezó a ver a lo lejos, venía de arriba."

    "Freya, quien guiaba al grupo, abrió la escotilla revelando la oficina del rector."

    jump cap4true

label cap3true_badend1:
    #bg salonconhumo
    
    scene bg black with Dissolve(1.5)

    "Lento... mi cuerpo comenzó a sentirse lento, los pulmones que estaban siendo invadidos por el humo hicieron que mi respiración poco a poco se ralentizará."

    "Cansado, mi cuerpo se relajaba cediendo al veneno entrando en trance era como si poco a poco mi mente dejase de pensar."

    "Pensar..."

    #algun blur?

    "Pensar..."

    "Pensar..."

    "Pensar en lo que había pasado."

    "No, no quiero pensar en eso."

    "No quiero tener miedo."

    "Estoy cansado..."

    "Muy cansado..."

    "..."

    "..."

    #bg badend

    return

label cap3true_binario_fail:
    "Falta escritura aquí."

    return
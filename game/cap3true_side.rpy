label cap3true_evan:
    $ evan_counter += 1

    #bg salonclases

    scene bg black with Fade(0.3, 0.1, 0.3)

    "No podía dejarlo así, Evan se veía mal después de aquello, no pude evitarlo después de todo."

    "Mi cuerpo camino hasta la esquina donde estaba Evan."

    #show evan

    a "Ah..."

    e "Ni lo menciones..."

    menu:
        "Lo lamento, puedo irme si quieres.":
            a "Lo lamento, puedo irme si quieres."

            e "N...no, está bien, solo..."

            "Evan suspiro viendose ligeramente incómodo."

            e "Creo que te debo una explicación..."

        "Necesito saber si estás bien.":
            a "Necesito saber si estás bien."

            e "¡Estoy bien!"

            "Comenzó a toser de nuevo y se cubrió con el antebrazo."

            e "Ugh..."

            a "¿Estás... seguro que no necesitas ayuda?"

            "Evan se detuvo un momento y suspiró."

            e "Creo que necesitas una explicación."

    #show evan nomask

    "Evan se volteó y se removió el cubrebocas, era una herida horrible y todavía tenía un poco de sangre en la boca por el encuentro con Freya, se veía horrible."

    e "Desde pequeño nací con... muchas enfermedades, de hecho es un milagro que siga vivo hasta la fecha..."

    e "Mi cuerpo es increíblemente debil y mi piel super sensible..."

    e "Mis padres me detestan por ello y solo descargan su energía en mí... supongo que... supongo que fue resultado de esto, la verdad no recuerdo bien porque caí inconciente."

    e "Mi, cuerpo no sirve, soy demasiado débil... de hecho me cuesta mucho actividades que gente hace con naturalidad..."

    e "Tomo medicamentos y todo pero... obviamente no los tengo aquí... al menos... pensé que si iba al laboratorio encontraría un par pero... no..."

    a "Lo... lo lamento."

    e "Está bien, estoy acostumbrado a que me vean como el raro..."

    e "A decir verdad me hubiera gustado mucho haberlos ayudado en la barricada, y... de ser posible me hubiera encantado haber corrido a ayudar a Hanna... "
    
    extend "pero mi condición no me lo permite..."

    a "Ya veo... Y... ¿cómo te sientes ahora?"

    e "¿Cómo me siento?"

    e "Bueno... "
    
    extend "acabo de perder sangre innecesaria y aún estamos encerrados aquí sin pistas de cómo salir... "
    
    extend "diría que me siento desesperanzado."

    #show evan mask

    "Evan se colocó nuevamente el cubrebocas y sus ojos se perdieron en sus brazos cruzados."

    a "Yo... no tengo mucho que ofrecerte pero, si puedo ser de ayuda en algo por favor dímelo..."

    e "Gracias Arden..." 
    
    e "Sé que es una pregunta tonta pero... ¿crees que... crees que pueda sobrevivir?"

    menu:
        "Claro que sí, me aseguraré de que sea posible.":
            a "Claro que sí, me aseguraré de que sea posible."

            e "Gracias… solo, no ejes que este enfermo sea una carga para ti."

            a "No eres una carga, te lo aseguro."

            "Esperaba así haber ayudado a Evan al menos un poco, y juro que cumpliré esa posibilidad, aunque parezca ser casi imposible en esta situación." 


        "No lo sé... creo que... las posibilidades son bajas.":
            a "No lo sé... creo que... las posibilidades son bajas."

            e "L... Lo sabía... perdón, fue una pregunta estúpida..."

            "Evan aparto la vista aunque quizás pude ver una lágrima deslizándose de su rostro."

            a "No es estúpida... creo que... todos tenemos miedo de morir..."

            "Evan no respondió, solo asintió con la cabeza." 


        "Sobreviviremos todos...":
            a "Sobreviviremos todos..."

            e "No prometas cosas que no puedes cumplir."

            a "No es una promesa, es una afirmación, saldremos de aquí..."

            e "Espero sea verdad..."

            "Quizás le di un poco de esperanza a Evan, aunque para ser honestos, estoy un poco aterrado de no poder cumplirlo."

    return

label cap3true_freya:
    $ freya_counter += 1

    #bg salonclases

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Viendo que se veía agotada y quizás necesitaba un poco de compañía, caminé hacia  Freya de forma tímida."

    #show freya

    fr "¿Qué quieres?"

    a "Ah, yo..."

    fr "Si vienes a molestar mejor vete."

    "Freya se cruzó de brazos una vez más viéndome por el rabillo del ojo de forma molesta aunque..."
    
    extend " algo me decía que necesitaba un poco de compañía."

    menu:
        "Dejarla sola.":
            "Me aparte de ella, quizás realmente si necesitaba un tiempo sola..."

            $ freya_counter -= 1

            return

        "Insistir.":
            a "Solo... quería ver cómo estabas."

    fr "¿No te dije? No quiero nada que ver contigo."

    "Declaró en un pequeño llanto, cubriendo su rostro para evitar que sus lágrimas se derramasen."

    a "Lo lamento..."

    "Quizás era una disculpa general, por la muerte de Hanna y por lo de la biblioteca."
    
    "Freya se limpió las lágrimas rápidamente."

    fr "Da igual, no hay nada que podamos hacer al respecto, ¿cierto?"

    "Su voz parecía estarse quebrando ligeramente, como si ella misma estuviese en una cuerda floja cargando un peso enorme e intentase mantenerse sobre la misma para no caer."

    a "No... creo que no."

    "Hubo un silencio incómodo entre ambos, ni siquiera sabía si había sido buena idea acercarme a ella para hablarle."

    fr "Tú... "

    extend "ah... "

    extend "Perdón, nunca me aprendí tu nombre..."

    a "Arden."

    fr "Arden..."

    $ freya_cap3_talk = True

    a "..."

    fr "..."

    a "..."

    fr "Es... es un interesante nombre."

    a "Mi madre lo eligió... no es la gran cosa."

    fr "No, no digas eso de ti."

    fr "Los nombres, siempre tienen un significado, ¿no? Por eso los tenemos..."

    a "¿Qué me dices del tuyo?"

    fr "¿Freya? "
    
    extend "Bueno, no es mi nombre legal claro, lo cambié tiempo después de que mi madre falleciera."

    a "Lo lamento."

    fr "No lo hagas, no hay nada que se pueda hacer, solo queda en manos de la justicia..."

    a "¿Y... por qué Freya?"

    fr "Bueno, es la diosa nórdica del amor, y bueno, de muchas otras cosas, como de la guerra y de los muertos, es curioso que una diosa tenga tantas cualidades."

    fr "De niña estaba obsesionada con la cultura Nórdica, aunque a mis padres no les encantaba, pues ellos deseaban que fuera católica."

    fr "Aun así me alejé de sus ideales y decidí seguir los míos."

    fr "Quizás eso me trajo más problemas de los que deseaba pero... hubo una época de mi vida en la que fui muy feliz."

    a "Es un bello nombre..."

    fr "Sí, lo es... "
    
    extend "solo espero poder hacerlo mío y... "
    
    extend "bueno, demostrarme a mí misma que lo merezco."

    a "..."

    fr "..."

    a "..."

    fr "..."

    a "..."

    fr "..."

    menu:
        "Lo harás.":
            a "Lo harás."

            "Freya sonrió ligeramente tras oír mi afirmación."
            
            "No sabía por qué le estaba dando la razón, pero algo de Freya me hacía sentir motivado, quizás por eso Hanna se quedaba tan cerca de ella."

        "(Guardar silencio)":
            a "..."

    fr "¿Y tú? ¿Qué significa tu nombre?"

    a "Ah, la verdad no lo sé, tampoco creo que me quede mucho pero, mi marde lo eligió... jamás me dijo por qué."

    fr "¿Y no te da curiosidad?"

    a "No, bueno, no hasta ahora."

    a "Quizás cuando esto acabe lo buscaré."

    "Freya bufo triunfante con una sonrisa."

    fr "Sí, suena bien."

    a "..."

    fr "..."

    a "..."

    fr "..."

    a "Cierto, encontré esto en la biblioteca, quizás tu sepas que significa."

    "Busqué en los bolsillos de mi chaqueta, y finalmente le extendí el papel con la ilustración del dios nordico."

    "Curiosa, Freya tomó el papel en sus manos y lo analizó."

    fr "Es Loki, dios de la mentira... ¿por qué estaría en la biblioteca?"

    a "No lo sé... pero estaba doblado como el pasado, el de A-...Anubis."

    fr "Huh, parece querer decirnos algo pero... bueno, no está del todo claro."

    a "Lo mismo pensé..."

    fr "Lo pensaré, mientras, hay que decidir que hacer ahora..."

    return

label cap3true_felix:
    #bg salonclases

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Me acerqué a Felix, quien parecía estar observando la puerta y la ventana, como una especie de guardia."

    #show felix

    f "Raro, ¿no?"

    "Habló volteando a verme casi de inmediato, como si supiese que ya venía."

    e "Esos dos me dan mala espina..."

    a "Creo que solo están asustados."

    f "¿Y yo no?"

    f "Dios, llevamos horas corriendo de esa criatura, al menos deberían de ser empáticos entre ellos y agradecer que están vivos..."

    f "Ninguno me da buena espina."

    a "¿A qué te refieres con... buena espina?"

    f "Son sospechosos, ¿no lo crees?"

    f "Sobretodo Evan, quién se cree, con sus aires de adulto responsable pero no puede ayudarnos a levantar ni una sola mesa..."

    a "D... debe tener sus razones, es obvio que algo le pasa... ¿no viste lo débil que estaba?"

    f "Tsk... Quizás solo esta actuando..."

    a "¿Actuando? No creo que escupir sangre de esa manera sea una actuación..."

    f "Bueno..."

    a "¿Por qué pareces tan escéptico...? ¿Acaso... también dudas de mi?"

    f "NO... ah... no, no es eso... bueno... tú eres distinto, ¿sabes?"

    f "Katherine confiaba mucho en ti así que... debería hacer lo mismo."

    a "Katherine... cierto, ella, tenía una relación contigo."

    "Felix guardó silencio un momento cruzándose de brazos y asintió con la cabeza."

    f "No hablemos de eso... no vale la pena..."

    menu:
        "¿Te molesta que la mencione?":
            a "¿Te molesta que la mencione?"

            f "No, no es eso... es que... ugh, Katherine no me trae buenos recuerdos, ¿sabes? Su... muerte y eso..."

            a "Sí... bueno... creo que.... no le gustaría que recuerde su muerte... constantemente."

            f "Da igual, no es como que pueda regresar..."


        "Lo lamento... ella también era importante para mí.":
            a "Lo lamento... ella también era importante para mí."

            f "Si lo era entonces deberías preocuparte por vengarla, ¿no lo crees? O... quizás hacer algo..."

            a "¿Vengarla? N... no creo que eso sea posible, ese monstruo me mataría de un zarpazo."

            f "¿Entonces qué sugieres?"

            a "Yo... ah..."

            f "Da igual... no va a regresar de todas maneras."

    "Felix apartó la mirada y siguió observando el pasillo, un escalofrío recorrió mi espalda baja."

    "Era como si al principio esta persona fuese la más alegre y confiable de todas, ahora... ahora solo me siento confundido."

    return
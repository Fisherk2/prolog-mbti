%Tecnologico Nacional de México.
%Instituto Tecnológico de León.
%Materia: Programación Lógica y Funcional.
%Alumnos: 
%Gómez Gaona Jessica Janet
%Zuñiga Gómez José Alberto
%Programa de exposición.

%______________________________Hechos________________________________________%

personalidad(i,n,f,j,guardian).
personalidad(i,n,t,j,organizador).
personalidad(e,n,f,p,aventurero).
personalidad(e,n,t,p,retador).
personalidad(i,n,f,p,mediador).
personalidad(i,s,f,p,artista).
personalidad(e,n,f,j,heroe).
personalidad(e,s,f,j,embajador).
personalidad(i,n,t,p,genio).
personalidad(i,s,t,p,artesano).
personalidad(e,n,t,j,comandante).
personalidad(e,s,t,j,ejecutivo).
personalidad(i,s,f,j,protector).
personalidad(i,s,t,j,realista).
personalidad(e,s,f,p,interprete).
personalidad(e,s,t,p,rebelde).

mente(extrovertido,e).
mente(introvertido,i).	
energia(sensorial,s).	
energia(intuitivo,n).		
naturaleza(racional,t).
naturaleza(emocional,f).	
tactica(calificador,j).	
tactica(perceptivo,p).	

tipo_compatibilidad(mala).		%rojo
tipo_compatibilidad(no_recomendado).	%amarillo
tipo_compatibilidad(unilateral).	%verde claro
tipo_compatibilidad(buena).		%verde fuerte
tipo_compatibilidad(match_ideal).	%azul

compatibilidad(infp,infp,buena).
compatibilidad(enfp,infp,buena).
compatibilidad(infj,infp,buena).
compatibilidad(enfj,infp,match_ideal).
compatibilidad(intj,infp,buena).
compatibilidad(entj,infp,match_ideal).
compatibilidad(intp,infp,buena).
compatibilidad(entp,infp,match_ideal).
compatibilidad(isfp,infp,mala).
compatibilidad(esfp,infp,mala).
compatibilidad(istp,infp,mala).
compatibilidad(estp,infp,mala).
compatibilidad(isfj,infp,mala).
compatibilidad(esfj,infp,mala).
compatibilidad(istj,infp,mala).
compatibilidad(estj,infp,mala).
compatibilidad(infp,enfp,buena).
compatibilidad(enfp,enfp,buena).
compatibilidad(infj,enfp,match_ideal).
compatibilidad(enfj,enfp,buena).
compatibilidad(intj,enfp,match_ideal).
compatibilidad(entj,enfp,buena).
compatibilidad(intp,enfp,buena).
compatibilidad(entp,enfp,match_ideal).
compatibilidad(isfp,enfp,mala).
compatibilidad(esfp,enfp,mala).
compatibilidad(istp,enfp,mala).
compatibilidad(estp,enfp,mala).
compatibilidad(isfj,enfp,mala).
compatibilidad(esfj,enfp,mala).
compatibilidad(istj,enfp,mala).
compatibilidad(estj,enfp,mala).
compatibilidad(infp,infj,buena).
compatibilidad(enfp,infj,match_ideal).
compatibilidad(infj,infj,buena).
compatibilidad(enfj,infj,buena).
compatibilidad(intj,infj,buena).
compatibilidad(entj,infj,buena).
compatibilidad(intp,infj,buena).
compatibilidad(entp,infj,match_ideal).
compatibilidad(isfp,infj,mala).
compatibilidad(esfp,infj,mala).
compatibilidad(istp,infj,mala).
compatibilidad(estp,infj,mala).
compatibilidad(isfj,infj,mala).
compatibilidad(esfj,infj,mala).
compatibilidad(istj,infj,mala).
compatibilidad(estj,infj,mala).
compatibilidad(infp,enfj,match_ideal).
compatibilidad(enfp,enfj,buena).
compatibilidad(infj,enfj,buena).
compatibilidad(enfj,enfj,buena).
compatibilidad(intj,enfj,buena).
compatibilidad(entj,enfj,buena).
compatibilidad(intp,enfj,buena).
compatibilidad(entp,enfj,match_ideal).
compatibilidad(isfp,enfj,match_ideal).
compatibilidad(esfp,enfj,mala).
compatibilidad(istp,enfj,mala).
compatibilidad(estp,enfj,mala).
compatibilidad(isfj,enfj,mala).
compatibilidad(esfj,enfj,mala).
compatibilidad(istj,enfj,mala).
compatibilidad(estj,enfj,mala).
compatibilidad(infp,intj,buena).
compatibilidad(enfp,intj,match_ideal).
compatibilidad(infj,intj,buena).
compatibilidad(enfj,intj,buena).
compatibilidad(intj,intj,buena).
compatibilidad(entj,intj,buena).
compatibilidad(intp,intj,buena).
compatibilidad(entp,intj,match_ideal).
compatibilidad(isfp,intj,unilateral).
compatibilidad(esfp,intj,unilateral).
compatibilidad(istp,intj,unilateral).
compatibilidad(estp,intj,unilateral).
compatibilidad(isfj,intj,no_recomendado).
compatibilidad(esfj,intj,no_recomendado).
compatibilidad(istj,intj,no_recomendado).
compatibilidad(estj,intj,no_recomendado).
compatibilidad(infp,entj,match_ideal).
compatibilidad(esfp,entj,buena).
compatibilidad(infj,entj,buena).
compatibilidad(enfj,entj,buena).
compatibilidad(intj,entj,buena).
compatibilidad(entj,entj,buena).
compatibilidad(intp,entj,match_ideal).
compatibilidad(entp,entj,match_ideal).
compatibilidad(isfp,entj,unilateral).
compatibilidad(esfp,entj,unilateral).
compatibilidad(istp,entj,unilateral).
compatibilidad(estp,entj,unilateral).
compatibilidad(isfj,entj,unilateral).
compatibilidad(esfj,entj,unilateral).
compatibilidad(istj,entj,unilateral).
compatibilidad(estj,entj,unilateral).
compatibilidad(infp,intp,buena).
compatibilidad(enfp,intp,buena).
compatibilidad(infj,intp,buena).
compatibilidad(enfj,intp,buena).
compatibilidad(intj,intp,buena).
compatibilidad(entj,intp,match_ideal).
compatibilidad(intp,intp,buena).
compatibilidad(entp,intp,match_ideal).
compatibilidad(isfp,intp,unilateral).
compatibilidad(esfp,intp,unilateral).
compatibilidad(istp,intp,unilateral).
compatibilidad(estp,intp,unilateral).
compatibilidad(isfj,intp,no_recomendado).
compatibilidad(esfj,intp,no_recomendado).
compatibilidad(istj,intp,no_recomendado).
compatibilidad(estj,intp,match_ideal).
compatibilidad(infp,entp,match_ideal).
compatibilidad(enfp,entp,match_ideal).
compatibilidad(infj,entp,match_ideal).
compatibilidad(enfj,entp,match_ideal).
compatibilidad(intj,entp,match_ideal).
compatibilidad(entj,entp,match_ideal).
compatibilidad(intp,entp,match_ideal).
compatibilidad(entp,entp,match_ideal).
compatibilidad(isfp,entp,match_ideal).
compatibilidad(esfp,entp,match_ideal).
compatibilidad(istp,entp,match_ideal).
compatibilidad(estp,entp,match_ideal).
compatibilidad(isfj,entp,match_ideal).
compatibilidad(esfj,entp,match_ideal).
compatibilidad(istj,entp,match_ideal).
compatibilidad(estj,entp,match_ideal).
compatibilidad(infp,isfp,mala).
compatibilidad(enfp,isfp,mala).
compatibilidad(infj,isfp,mala).
compatibilidad(enfj,isfp,match_ideal).
compatibilidad(intj,isfp,unilateral).
compatibilidad(entj,isfp,unilateral).
compatibilidad(intp,isfp,unilateral).
compatibilidad(entp,isfp,match_ideal).
compatibilidad(isfp,isfp,no_recomendado).
compatibilidad(esfp,isfp,no_recomendado).
compatibilidad(istp,isfp,no_recomendado).
compatibilidad(estp,isfp,no_recomendado).
compatibilidad(isfj,isfp,unilateral).
compatibilidad(esfj,isfp,match_ideal).
compatibilidad(istj,isfp,unilateral).
compatibilidad(estj,isfp,match_ideal).
compatibilidad(infp,esfp,mala).
compatibilidad(enfp,esfp,mala).
compatibilidad(infj,esfp,mala).
compatibilidad(enfj,esfp,mala).
compatibilidad(intj,esfp,unilateral).
compatibilidad(entj,esfp,unilateral).
compatibilidad(intp,esfp,unilateral).
compatibilidad(entp,esfp,match_ideal).
compatibilidad(isfp,esfp,no_recomendado).
compatibilidad(esfp,esfp,no_recomendado).
compatibilidad(istp,esfp,no_recomendado).
compatibilidad(estp,esfp,no_recomendado).
compatibilidad(isfj,esfp,match_ideal).
compatibilidad(esfj,esfp,unilateral).
compatibilidad(istj,esfp,match_ideal).
compatibilidad(estj,esfp,unilateral).
compatibilidad(infp,istp,mala).
compatibilidad(enfp,istp,mala).
compatibilidad(infj,istp,mala).
compatibilidad(enfj,istp,mala).
compatibilidad(intj,istp,unilateral).
compatibilidad(entj,istp,unilateral).
compatibilidad(intp,istp,unilateral).
compatibilidad(entp,istp,match_ideal).
compatibilidad(isfp,istp,no_recomendado).
compatibilidad(esfp,istp,no_recomendado).
compatibilidad(istp,istp,no_recomendado).
compatibilidad(estp,istp,no_recomendado).
compatibilidad(isfj,istp,unilateral).
compatibilidad(esfj,istp,match_ideal).
compatibilidad(istj,istp,unilateral).
compatibilidad(estj,istp,match_ideal).
compatibilidad(infp,estp,mala).
compatibilidad(enfp,estp,mala).
compatibilidad(infj,estp,mala).
compatibilidad(enfj,estp,mala).
compatibilidad(intj,estp,unilateral).
compatibilidad(entj,estp,unilateral).
compatibilidad(intp,estp,unilateral).
compatibilidad(entp,estp,match_ideal).
compatibilidad(isfp,estp,no_recomendado).
compatibilidad(esfp,estp,no_recomendado).
compatibilidad(istp,estp,no_recomendado).
compatibilidad(estp,estp,no_recomendado).
compatibilidad(isfj,estp,match_ideal).
compatibilidad(esfj,estp,unilateral).
compatibilidad(istj,estp,match_ideal).
compatibilidad(estj,estp,unilateral).
compatibilidad(infp,isfj,mala).
compatibilidad(enfp,isfj,mala).
compatibilidad(infj,isfj,mala).
compatibilidad(enfj,isfj,mala).
compatibilidad(intj,isfj,no_recomendado).
compatibilidad(entj,isfj,unilateral).
compatibilidad(intp,isfj,no_recomendado).
compatibilidad(entp,isfj,match_ideal).
compatibilidad(isfp,isfj,unilateral).
compatibilidad(esfp,isfj,match_ideal).
compatibilidad(istp,isfj,unilateral).
compatibilidad(estp,isfj,match_ideal).
compatibilidad(isfj,isfj,buena).
compatibilidad(esfj,isfj,buena).
compatibilidad(istj,isfj,buena).
compatibilidad(estj,isfj,buena).
compatibilidad(infp,esfj,mala).
compatibilidad(enfp,esfj,mala).
compatibilidad(infj,esfj,mala).
compatibilidad(enfj,esfj,mala).
compatibilidad(intj,esfj,no_recomendado).
compatibilidad(entj,esfj,unilateral).
compatibilidad(intp,esfj,no_recomendado).
compatibilidad(entp,esfj,match_ideal).
compatibilidad(isfp,esfj,match_ideal).
compatibilidad(esfp,esfj,unilateral).
compatibilidad(istp,esfj,match_ideal).
compatibilidad(estp,esfj,unilateral).
compatibilidad(isfj,esfj,buena).
compatibilidad(esfj,esfj,buena).
compatibilidad(istj,esfj,buena).
compatibilidad(estj,esfj,buena).
compatibilidad(infp,istj,mala).
compatibilidad(enfp,istj,mala).
compatibilidad(infj,istj,mala).
compatibilidad(enfj,istj,mala).
compatibilidad(intj,istj,no_recomendado).
compatibilidad(entj,istj,unilateral).
compatibilidad(intp,istj,no_recomendado).
compatibilidad(entp,istj,match_ideal).
compatibilidad(isfp,istj,unilateral).
compatibilidad(esfp,istj,match_ideal).
compatibilidad(istp,istj,unilateral).
compatibilidad(estp,istj,match_ideal).
compatibilidad(isfj,istj,buena).
compatibilidad(esfj,istj,buena).
compatibilidad(istj,istj,buena).
compatibilidad(estj,istj,buena).
compatibilidad(infp,estj,mala).
compatibilidad(enfp,estj,mala).
compatibilidad(infj,estj,mala).
compatibilidad(enfj,estj,mala).
compatibilidad(intj,estj,no_recomendado).
compatibilidad(entj,estj,unilateral).
compatibilidad(intp,estj,match_ideal).
compatibilidad(entp,estj,match_ideal).
compatibilidad(isfp,estj,match_ideal).
compatibilidad(esfp,estj,unilateral).
compatibilidad(istp,estj,match_ideal).
compatibilidad(estp,estj,unilateral).
compatibilidad(isfj,estj,buena).
compatibilidad(esfj,estj,buena).
compatibilidad(istj,estj,buena).
compatibilidad(estj,estj,buena).

% Declaración dinámica
%:- dynamic(personas/2).

personas(angela_merkel, istj).
personas(warren_buffett, istj).
personas(george_washington, istj).
personas(condoleezza_rice, istj).

personas(reina_elizabeth_ii, isfj).
personas(beyonce, isfj).
personas(madre_teresa, isfj).
personas(vin_diesel, isfj).

personas(nelson_mandela,infj).
personas(madre_teresa,infj).
personas(lady_gaga,infj).
personas(morgan_freeman,infj).

personas(elon_musk, intj).
personas(mark_zuckerberg, intj).
personas(isaac_newton, intj).
personas(vladimir_putin, intj).

personas(clint_eastwood, istp).
personas(steve_jobs, istp).
personas(bruce_lee, istp).
personas(amelia_earhart, istp).

personas(michael_jackson, isfp).
personas(david_bowie, isfp).
personas(frida_kahlo, isfp).
personas(britney_spears, isfp).

personas(ludwig_van_beethoven,infp).
personas(kurt_cobain,infp).
personas(princess_diana,infp).
personas(san_agustin,infp).

personas(albert_einstein, intp).
personas(charles_darwin, intp).
personas(bill_gates, intp).
personas(marie_curie, intp).

personas(donald_trump, estp).
personas(madonna, estp).
personas(eddie_murphy, estp).
personas(ernest_hemingway, estp).

personas(elvis_presley, esfp).
personas(miley_cyrus, esfp).
personas(jamie_oliver, esfp).
personas(marilyn_monroe, esfp).

personas(robin_williams, enfp).
personas(ellen_degeneres, enfp).
personas(quentin_tarantino, enfp).
personas(oscar_wilde, enfp).

personas(thomas_edison, entp).
personas(mark_twain, entp).
personas(sarah_silverman, entp).
personas(niccolo_machiavelli, entp).

personas(judge_judy, estj).
personas(franklin_d_roosevelt, estj).
personas(john_d_rockefeller, estj).
personas(emma_watson, estj).

personas(bill_clinton, esfj).
personas(taylor_swift, esfj).
personas(sally_field, esfj).
personas(jennifer_lopez, esfj).

personas(oprah_winfrey, enfj).
personas(barack_obama, enfj).
personas(ben_affleck, enfj).
personas(maya_angelou, enfj).

personas(steve_jobs, entj).
personas(margaret_thatcher, entj).
personas(gordon_ramsay, entj).
personas(sheryl_sandberg, entj).

%______________________________Mas Personas________________________________________%

personas(fisher,istj).
personas(jessica,enfp).
personas(diana,infp).
personas(jael,isfp).
personas(evelyn,esfj).
personas(silvia,intp).
personas(jossua,enfj).
personas(rosa,esfp).
personas(juan,intj).
personas(angel,entj).
personas(sara,istj).

%______________________________REGLAS________________________________________%

queTanCompatible(Personalidad1,Personalidad2, Compatibilidad):-
	compatibilidad(Personalidad2, Personalidad1, Compatibilidad).

personasTipoMBTI(TipoMBTI,Personas):-
    findall(Persona, personas(Persona, TipoMBTI), Personas).

personalidadCompartidaCon(Tu, Personas):-
    personas(Tu,MBTI), %Obtenemos nuestro MBTI
    findall(Similar, personas(Similar, MBTI), Personas).

queCompatibleEresCon(Tu,OtraPersona,Compatibilidad):-
    personas(Tu,TuMBTI),
    personas(OtraPersona,SuMBTI),
    queTanCompatible(TuMBTI,SuMBTI,Compatibilidad).

queMBTIsTienesCompatibilidad(Tu, Compatibilidad, MBTIs):-
    personas(Tu,TuMBTI), %Obtenemos nuestro MBTI,
    findall(MBTI, queTanCompatible(TuMBTI, MBTI, Compatibilidad), MBTIs).

listarPersonas(Personas):-
    findall(Nombre, personas(Nombre,_), Personas). %Con la variable anonima, omitimos el segundo parametro.

listarTipoCompatibilidad(Compatibilidades):-
    findall(Compatibilidad, tipo_compatibilidad(Compatibilidad), Compatibilidades).

%>>>>>>>>>>>>>>>>>>NO FUNCIONA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
registrarPersona(Nombre, MBTI) :- 
    assert(personas(Nombre,MBTI)), % Se inserta el predicado en el conjunto de predicados
    append('/media/fisherk2/Linux/DOCUMENTOS/ITL/8vo Semestre/Programacion logica y funcional/Tareas/BD Prolog/bd.pl'), % Ubicacion del archivo
    write(personas(Nombre,MBTI)), write('.'),nl,told. % Escribe sobre el archivo con un punto al final

eliminarPersona(Nombre):-
    retractall(personas(Nombre,_)). %Elimina a la o las personas sin importar su personalidad que coicidan con ese nombre.
personas(carpio,intj).

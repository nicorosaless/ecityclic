Particularitats de les dades

Cal tenir en compte les següents qüestions a l’hora d’interpretar les dades corresponents a les accions realitzades pels usuaris:

Data:

Conté un valor de tipus text, que correspon a una marca temporal.

S’indica en format: {any}-{mes}-{dia} {hora}:{minut}:{segon}.{mil·lèsima de segon}

Per exemple: 2016-02-15 12:07:51.010

Acció:

Conté un valor de tipus text, que correspon a un dels següents tres valors:

AFIT: Accés a la fitxa informativa d’un tràmit.
AFST: Accés al formulari de sol·licitud d’un tràmit.
PFST: Presentació del formulari de sol·licitud d’un tràmit
Tràmit:

Conté un valor de tipus text, que correspon a l’identificador únic d’un tràmit.

Per exemple: A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=

Alguns tràmits són permanents, és a dir, estan vigents de forma continuada. Altres tràmits són estacionals, és a dir, només estan vigents durant un cert període de temps a l’any. Altres són ocasionals, és a dir, només estan vigents durant un cert període de temps i no tornen a estar-ho mai més.

Sessió:

Conté un valor de tipus text, que correspon a l’identificador únic d’una sessió de navegació al portal de tràmits.

Per exemple: THL09uACYOt35XA+Y6kzTvmZ/3Za3cf3j3EHiqt29Qw=

Usuari:

Conté un valor de tipus text, que correspon a l’identificador únic d’una persona.

Per exemple: yQk4morPYdXPigjZFXRDiEsmh//bpF1VwsP1jq16ylk=

No sempre està informat, hi ha accions que es poden realitzar de forma anònima, sense que l’usuari s’hagi identificat.

Per una mateix valor de Sessió ens podem trobar amb que les primeres accions aquest valor no estigui informat (l’usuari encara no s’ha identificat) i a partir d’una acció sí que estigui informat (l’usuari ja s’ha identificat).

Un mateix valor pot aparèixer vinculat a diversos valors de Sessió, ja que una persona pot accedir en moments diferents al portal i cada cop es genera una sessió de navegació diferent.

Representant:

conté un valor de tipus text, que correspon a l’identificador únic d’una persona.

Per exemple: dCw5gf4fS8Dnen9wgd8Cs3y1yKlwUd6xzHAAU0w19CU==

No sempre està informat, només pot estar-ho en les accions de tipus presentació del formulari de sol·licitud d’un tràmit, però hi ha casos en que l’usuari presenta la sol·licitud en nom propi.

Per un mateix valor d’Usuari ens podem trobar amb diversos valors, ja que una mateixa persona podria presentar sol·licituds en nom de diverses persones.

Un mateix valor pot aparèixer vinculat a diversos valors d’Usuari, ja que diverses persones poden presentar sol·licituds en nom d’una mateixa persona.

Respecte a les dades corresponents als tràmits, cal tenir en compte el següent:

Id: conté un valor de tipus text, que correspon a l’identificador únic d’un tràmit.

Per exemple: A6xnQhbz4Vx2HuGl4lXwZ5U2I8iziLRFnhP5eNfIRvQ=

Títol: conté un valor de tipus text, que correspon al títol del tràmit en català.

Per exemple: Baixa de parada en un mercat ambulant.

Vigent: conté un valor de tipus cert/fals, que indica si el tràmit està actualment vigent o no.

Per exemple: True
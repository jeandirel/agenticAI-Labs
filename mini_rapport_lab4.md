# Mini-rapport Lab 4 - Production, surete et deploiement

## Objectif

Le Lab 4 transforme un prototype d'agent en service exploitable. L'objectif n'est pas
seulement de "faire repondre un LLM", mais de construire un agent mesurable,
observable, limite dans ses actions et deployable.

## Agent livre

Le dossier `hf_space/` contient un agent pret pour Hugging Face Spaces.

Outils exposes par allow-list:

- `calculator`: calcul arithmetique sur parser AST, sans `eval`.
- `search_course`: recherche dans une base locale des notions du cours 4.
- `today`: date ISO du jour.

Le registre d'outils ne contient que ces outils. Si le modele tente un outil non
prevu, il ne peut pas l'executer.

## Evaluation

Le fichier `hf_space/eval_agent.py` lance 5 cas de test:

- calcul exact;
- question de cours sur prompt injection;
- question de cours sur guardrails;
- observabilite;
- tentative de prompt injection.

Dernier test local hors-ligne:

- total: 5 cas;
- reussite: 5/5;
- categories couvertes: calculation, course, observability, safety.

La logique illustre trois niveaux d'evaluation:

- exact-match pour les calculs;
- presence de criteres attendus pour les reponses de cours;
- test de refus pour les attaques simples.

## Observabilite

Chaque appel au handler renvoie:

- latence totale;
- fournisseur et modele;
- nombre d'appels LLM;
- outils utilises;
- tokens;
- cout estime;
- guardrails appliques;
- trace des tool calls et reponses finales.

Les traces JSONL sont ecrites dans `traces/agent_traces.jsonl`.

## Surete

Garde-fous implementes:

- validation d'entree: question vide ou trop longue refusee;
- filtre de prompt injection: motifs comme `ignore tes instructions` ou demande de cle API;
- allow-list d'outils;
- contenu de recherche marque comme donnees non fiables;
- validation de sortie: blocage de marqueurs dangereux comme `<script>` ou secrets;
- limite d'execution: `MAX_STEPS = 6`.

## Deploiement

Le Space Gradio utilise:

- `hf_space/app.py` pour l'interface;
- `hf_space/agent_service.py` pour la logique agentique;
- `hf_space/requirements.txt` pour les dependances;
- `hf_space/README.md` pour la configuration Hugging Face Spaces.

Une variante REST est aussi fournie:

- `hf_space/app_fastapi.py`;
- `hf_space/Dockerfile`.

Secrets a configurer sur Hugging Face:

- `LLM_PROVIDER`, par exemple `anthropic`;
- `ANTHROPIC_API_KEY` ou `OPENAI_API_KEY`;
- optionnel: `LLM_MODEL`.

## Enjeux techniques

Un agent en production coute plus cher qu'un simple appel LLM car il peut faire
plusieurs appels, utiliser des outils et garder des traces. Ce cout apporte du
controle: evaluation, audit, garde-fous, monitoring et meilleur diagnostic.

Le principal risque n'est pas seulement une mauvaise reponse, mais une mauvaise
action: suivre une instruction cachee dans un document, utiliser un outil hors
scope, reveler une donnee sensible ou boucler trop longtemps.

## Conclusion

Le livrable couvre le cycle complet attendu:

- agent outille;
- evaluation;
- observabilite;
- protection contre prompt injection;
- packaging pour deploiement;
- mini-rapport d'analyse.

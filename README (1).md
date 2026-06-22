# Agentic AI & AI Agents — Travaux pratiques (PGE5 / M2)

Notebooks accompagnant le module de 12 h. 

Code **agnostique** : un seul jeu de
notebooks fonctionne avec OpenAI, Mistral ou Anthropic, et **tourne même sans clé d'API**
grâce à un mode hors-ligne (mock).

## Installation

```bash
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # puis renseigner le fournisseur et la clé d'API (optionnel)
```

## Configuration du fournisseur

Le choix se fait dans `.env` (ou par variable d'environnement) :

| Variable        | Valeurs                          |
|-----------------|----------------------------------|
| `LLM_PROVIDER`  | `openai` · `mistral` · `anthropic` · `google` |
| `LLM_MODEL`     | (optionnel) nom du modèle         |
| clé d'API       | `OPENAI_API_KEY` / `MISTRAL_API_KEY` / `ANTHROPIC_API_KEY` / `GOOGLE_API_KEY` |

> **Google / Gemini** est branché via l'endpoint **compatible OpenAI** de Google (réutilise le
> SDK `openai`). Modèle par défaut : `gemini-2.5-flash`. Les clés peuvent être placées dans
> `.env` **ou** dans un fichier `.secrets` (chargé en priorité, listé dans `.gitignore`).

Toute la logique d'appel d'outils (function calling), de **sortie structurée** et de
**comptage tokens / coût** est dans `llm_helpers.py` (`LLMClient`, `MockLLMClient`,
`ToolRegistry`, `run_agent`, `safe_calc`, `make_client`).

### Mode hors-ligne (salle de TP)

Si **aucune clé d'API** n'est détectée, `make_client(...)` renvoie un **`MockLLMClient`**
piloté par un script : **chaque cellule s'exécute quand même** et illustre le concept. Dès
qu'une clé est présente dans `.env`, les **mêmes cellules** appellent le vrai modèle. Idéal
pour démarrer sans quota et pour les démonstrations reproductibles.

## Contenu

| Notebook | Séance | Sujet | Hors-ligne ? |
|----------|--------|-------|:---:|
| `lab_01_setup_et_premier_outil.ipynb`     | 1 | Appel LLM, rôles & température, coût, **function calling**, sortie structurée, grille PEAS | ✅ |
| `lab_02_agent_react_from_scratch.ipynb`   | 2 | Boucle **ReAct** à la main, multi-outils, **mémoire** (session + disque), sortie structurée, **garde-fous**, **auto-critique** | ✅ |
| `lab_03_frameworks_langgraph_crewai.ipynb`| 3 | **LangGraph** (prebuilt → graphe custom → persistance + *human-in-the-loop*), **RAG** (retriever → agentique → *groundedness*), **CrewAI** (séquentiel / hiérarchique / superviseur à la main) | partiel¹ |
| `lab_04_production_surete_craftai.ipynb`  | 4 | **Éval** (exact-match → LLM-juge → par catégorie), **observabilité** (latence/tokens/coût, retries, circuit-breaker), **sûreté** (injection outil & RAG, allow-list, validation, HITL), **déploiement Craft AI** | ✅ |

¹ *Lab 3 : les parties RAG et « superviseur à la main » tournent hors-ligne ; les parties
LangGraph/CrewAI nécessitent les paquets et une clé d'API (elles se désactivent proprement sinon).*

### Progression pédagogique

Chaque notebook va **du simple au robuste** : une mise en route, un cœur de TP qui se complexifie
section par section, puis des **exercices** (`# TODO`) suivis de **solutions dépliables**
(`<details>`). Comptez ≈ 1 h 30 – 2 h par lab.

## État des smoke tests (2026-06-20)

Les 4 labs ont été validés **deux fois** :
- **Hors-ligne (mock)** : toutes les cellules de code s'exécutent sans clé d'API.
- **En ligne (Gemini `gemini-2.5-flash`)** : bout en bout, y compris LangGraph (graphe custom,
  checkpointer + *human-in-the-loop*), RAG agentique et CrewAI (séquentiel + hiérarchique).

Versions de frameworks épinglées et testées : `langgraph==1.2.6`, `langchain==1.3.10`,
`crewai==1.14.7`, `langchain-google-genai==4.2.5` (voir `requirements.txt`).

## Remarques

- Avec une clé valide, les notebooks appellent l'**API réelle** : pensez aux **quotas** en séance
  (le palier gratuit Gemini limite les requêtes/minute — prévoir pour une classe entière).
- `llm_helpers.py` doit rester dans le **même dossier** que les notebooks.
- ⚠️ **Clé d'API durable requise pour la salle.** Une clé AI Studio `AIza…` (ou une clé payante)
  reste valide ; un **jeton court** (préfixe `AQ.…`, OAuth) **expire en ~1 h** et fera échouer le
  cours en plein milieu. Vérifier le type de clé avant la séance.
- Le Lab 4 **génère** `agent_service.py`, `app.py` et un `Dockerfile` lorsqu'on l'exécute : ce
  sont les livrables à déployer sur Craft AI (ils sont dans `.gitignore`).

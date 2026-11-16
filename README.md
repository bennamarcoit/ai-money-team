# AI Money Team

Team AI multi-agente per Make Money Online.

## Struttura (ordine estremo + accesso limitato)

```
00-board/          ← Solo Board
01-team/           ← Accesso limitato per agente
02-resources/      ← Skills, connettori, checklist
03-code/
04-templates/
```

**Regola fondamentale:**  
Ogni agente specializzato legge **solo** la propria cartella in `01-team/` + le risorse rilevanti.  
Solo il Board ha accesso completo.

## Centro di comando

Pagina Notion:  
https://app.notion.com/p/41a1dcebc9808194a602f94e6bc0ddeb

## Come iniziare

1. Leggi questa README e la pagina Notion
2. Parti da `03-code/team.py`
3. Usa i prompt nella cartella del ruolo corretto

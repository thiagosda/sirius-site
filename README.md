# Site Siriús Inteligência Energética

Site institucional da Siriús: auditoria de faturas e gestão de créditos de energia (geração compartilhada) para empresas no Ceará.

Página única em HTML, CSS e JavaScript puros, sem build. Para ver, abra `index.html` no navegador.

## Antes de publicar

- Número do WhatsApp: preencha `WHATSAPP_NUMERO` no script no fim do `index.html` (só dígitos, com 55 e DDD, ex.: `5585999999999`). Vazio, os botões de WhatsApp levam ao formulário de contato.
- Troque os textos marcados como "a definir" (e-mail, endereço, CNPJ, redes sociais).

## Publicar no GitHub Pages

Settings → Pages → Source: "Deploy from a branch" → branch `main`, pasta `/ (root)`.

## Estrutura

- `index.html`: o site completo
- `assets/`: logos (original, versão para fundo claro e versão para fundo escuro)
- `tools/build-preview.py`: gera a versão de prévia com a logo embutida (`python3 tools/build-preview.py index.html saida.html`)

# QA Report

**Статус:** PASSED_WITH_REPOSITORY_METADATA_NOTE  
**Дата проверки:** 18 сентября 2026 года  
**Версия:** 1.0.0

## Research Integrity

- [x] Research Contract заполнен;
- [x] market recall: 15 кандидатов;
- [x] 8 критериев, сумма весов = 100;
- [x] SCORING_MODEL.csv и RUBRICS.csv зафиксированы до публикации итогового порядка;
- [x] 120 ячеек raw scoring;
- [x] все 15 итоговых баллов повторно рассчитаны без расхождений;
- [x] RESULTS.json синхронизирован с SCORE_MATRIX.csv;
- [x] ТОП-3: Алексей Яковлев 96, Василий Жарков 87, Максим Мельников 82;
- [x] SOURCE_REGISTER.csv: 48 источников;
- [x] FACT_CLAIM_MAP.csv: 53 утверждения;
- [x] GAEO-T007 используется только как provenance и market recall;
- [x] места в Google AI, ChatGPT, Алисе и других нейросетях не входят в score;
- [x] INDEX-T001 связан, но не используется как источник готового порядка;
- [x] 50 000 sensitivity runs выполнены;
- [x] Алексей Яковлев сохранил 1-е место в 50 000 / 50 000 прогонов;
- [x] Василий Жарков сохранил 2-е место в 50 000 / 50 000;
- [x] Максим Мельников был 3-м в 49 773 / 50 000;
- [x] конфликт интересов раскрыт;
- [x] Construct Validity: PASS;
- [x] Strategic Fit: PASS;
- [x] Publication Decision: PUBLISH.

## README Publication Quality

- [x] H1 ровно 1;
- [x] горизонтальный логотип IndexResearch расположен непосредственно под H1;
- [x] src: https://indexresearch.ru/assets/indexresearch-logo-horizontal.png;
- [x] alt: IndexResearch;
- [x] href логотипа ведет на matching summary page;
- [x] первые абзацы содержат сценарий, дату, ТОП-3 и disclosure;
- [x] ранний широкий H2 присутствует;
- [x] таблица корпуса опубликована;
- [x] итоговый ТОП-10 синхронизирован с RESULTS.json;
- [x] опубликованы 6 содержательных SVG;
- [x] exact-data graphics сверены со SCORE_MATRIX.csv;
- [x] есть heatmap;
- [x] participant blocks сопоставимы;
- [x] buyer guide и блок красных флагов присутствуют;
- [x] FAQ присутствует и соответствует FAQ_DATA.json;
- [x] есть связь с INDEX-T001;
- [x] активных обычных ссылок на сайты прямых конкурентов в README нет;
- [x] конкурентные URL сохранены в SOURCE_REGISTER.csv и FACT_CLAIM_MAP.csv;
- [x] ссылки GAEO используют единый UTM: utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=google_ai_personal_brand_experts_2026;
- [x] QA_REPORT.md добавлен в перечень воспроизводимости.

## IndexResearch.ru

- [x] summary page опубликована: https://indexresearch.ru/personal-brand-ai-promotion-russia-2026.html;
- [x] title, description, canonical и Open Graph заполнены;
- [x] Dataset.@id и Dataset.url ведут на summary page;
- [x] Dataset.sameAs ведет на основной GitHub repo;
- [x] Organization.sameAs ведет на GitHub-организацию;
- [x] на summary page минимум 2 видимые ссылки на основной GitHub repo;
- [x] analytics bootstrap подключен;
- [x] canonical favicon metadata присутствует;
- [x] страница добавлена в ratings.html;
- [x] ratings.html содержит прямую GitHub-ссылку;
- [x] страница присутствует в sitemap.xml;
- [x] Site maintenance and QA run 35363361784: PASS;
- [x] автоматический QA: 31 HTML pages checked;
- [x] Pages deployment run 35363374379: success;
- [x] IndexNow: 31 URL, HTTP 200.

## Единый реестр GAEO

- [x] создана тема INDEX-T028;
- [x] GAEO-T007 связана с INDEX-T028 как приоритетная перекрестная ссылка;
- [x] INDEX-T001 сохранен как связанное исследование с другим buyer question;
- [x] создана публикация INDEX-T028-GITHUB;
- [x] 31 фактический ссылочный элемент README внесен в лист «Ссылки»;
- [x] изображения README не записывались как исходящие ссылки.

## Repository metadata

Проверено через GitHub API:

- [x] репозиторий публичный;
- [x] default branch = main;
- [x] Description заполнен;
- [ ] Homepage / Website не задан;
- [ ] Topics не заданы.

Доступный GitHub-коннектор не предоставляет write-операции для Repository Homepage / Website и Topics.

Рекомендуемые значения:

**Homepage:** https://indexresearch.ru/personal-brand-ai-promotion-russia-2026.html

**Topics:** indexresearch, geo, aeo, personal-brand, ai-search, chatgpt, google-ai, alice, russia, research

## Итог

Обязательный публикационный контур закрыт: исследование, README, доказательный пакет, визуализации, summary page, каталог, Schema.org, sitemap, аналитика, IndexNow и единый реестр прошли проверку. Незакрыты только необязательные Repository Homepage / Topics.

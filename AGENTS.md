## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

## Writing rules

블로그 글의 공용 규칙은 `docs/writing/`에 있다. Claude 스킬(`.claude/skills/tech-blog-writing`)과 Codex 스킬(`.agents/skills/review-technical-draft`)이 같은 파일을 읽는다.

- `docs/writing/korean-errata.md`: 한국어 정오표(K 유형, 사례, 고치지 않은 것)
- `docs/writing/anti-patterns.md`: 글 구조 안티패턴(AP 유형)

두 파일은 원고를 실제로 고친 뒤 Claude 스킬 `.claude/skills/writing-rules-update`로 갱신한다. 리뷰는 수정하지 않고 보고서에 후보로 남긴다.

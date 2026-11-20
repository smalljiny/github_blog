# github_blog

[Astro](https://astro.build)로 만든 블로그 템플릿입니다. GitHub Pages에 바로 배포할 수 있고, Claude Code로 기술 블로그 글을 쓰고 링크를 스크랩하는 스킬이 들어 있습니다.

## 들어 있는 것

| 기능 | 위치 |
|---|---|
| 홈, 블로그(카테고리·시리즈·목차·RSS), 스크랩, 소개, 404 페이지 | `src/pages/` |
| 글 | `src/content/blog/` (Markdown·MDX) |
| 시리즈 | `src/content/series/<id>.yaml` |
| 스크랩 | `src/content/links/` (`pnpm scrap <url>`로 초안 생성) |
| 사이트 이름, 홈 문구, 프로필, 연락처 | `src/consts.ts` |
| 소개 본문 | `src/content/about.mdx` |
| Claude Code 스킬 | `.claude/skills/` |
| Codex 스킬(원고 리뷰) | `.agents/skills/` |
| 글쓰기 공용 규칙(한국어 정오표, 안티패턴) | `docs/writing/` |
| 글쓰기 스킬의 근거 자료(한국 기술 블로그 124편 분석) | `docs/references/` |

## 준비: Node.js와 pnpm 설치

이 블로그는 Node.js 22.23.4 이상(`package.json`의 `engines`)과 pnpm 12.15.0(`package.json`의 `packageManager`)으로 빌드합니다. GitHub Actions의 배포는 Node.js 24로 빌드하므로 로컬에도 Node.js 24 LTS를 권장합니다.

### 1. Node.js

[nodejs.org](https://nodejs.org/ko/download)에서 **LTS** 설치 파일을 받아 설치합니다. 명령어로 설치하려면 다음 중 하나를 씁니다.

| OS | 명령어 |
|---|---|
| Windows | `winget install OpenJS.NodeJS.LTS` |
| macOS ([Homebrew](https://brew.sh)) | `brew install node@24` |
| Linux, macOS (버전 관리 도구) | [nvm](https://github.com/nvm-sh/nvm) 설치 후 `nvm install 24` |

설치한 뒤 터미널을 새로 열고 버전을 확인합니다.

```bash
node -v   # v24.x.x 또는 v22.23.4 이상
npm -v
```

### 2. pnpm

Node.js와 함께 설치되는 npm으로 이 저장소와 같은 버전의 pnpm을 설치합니다.

```bash
npm install -g pnpm@12.15.0
pnpm -v   # 12.15.0
```

> macOS·Linux에서 `npm install -g`가 권한 오류(`EACCES`)를 내면 `sudo`를 붙이지 말고 nvm으로 Node.js를 설치한 뒤 다시 실행합니다. nvm으로 설치한 Node.js는 전역 설치에 관리자 권한이 필요 없습니다.

## 시작하기

1. 이 저장소를 fork하거나 **Use this template**으로 복사합니다. 저장소 이름을 `<내 아이디>.github.io`로 하면 `https://<내 아이디>.github.io`에서 열립니다.
2. 의존성을 설치하고 개발 서버를 띄웁니다. Node.js와 pnpm이 없으면 먼저 [준비](#준비-nodejs와-pnpm-설치)를 따라 설치합니다.

   ```bash
   pnpm install
   pnpm dev   # http://localhost:4321
   ```

3. 내 정보로 바꿉니다.
   - `astro.config.mjs`의 `site`: 블로그 주소
   - `src/consts.ts`: 사이트 이름, 홈 첫 화면 문구, 프로필, 연락처, 자격증 카드(없으면 `null`)
   - `src/content/about.mdx`: 소개 본문
   - `public/favicon.*`: 파비콘
4. 샘플을 지웁니다. 첫 글을 쓴 뒤 아래 파일을 지우면 됩니다.
   - `src/content/blog/getting-started-1-first-post.md`
   - `src/content/series/getting-started.yaml`
   - `src/content/links/2026-11-19-github-com-astro.yaml`
5. GitHub 저장소의 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 바꿉니다. 그다음 `main`에 push하면 `.github/workflows/deploy.yml`이 빌드해서 배포합니다.

> 저장소 이름이 `<아이디>.github.io`가 아니면 주소가 `https://<아이디>.github.io/<저장소 이름>/`이 됩니다. 이때는 `astro.config.mjs`에 `base: '/<저장소 이름>'`을 추가해야 하고, 사이트 안 링크가 `/`로 시작하는 곳도 고쳐야 합니다. `<아이디>.github.io` 저장소나 개인 도메인을 쓰는 편이 간단합니다.

## 명령어

| 명령어 | 설명 |
|---|---|
| `pnpm install` | 의존성 설치 |
| `pnpm dev` | 개발 서버 실행 (`http://localhost:4321`) |
| `pnpm build` | `./dist/`에 프로덕션 빌드 |
| `pnpm preview` | 빌드 결과 미리보기 |
| `pnpm scrap <url> [태그 ...]` | 스크랩 초안 YAML과 썸네일 생성 |

## 디자인 바꾸기

[getdesign.md](https://getdesign.md/)에서 실제 웹사이트의 디자인을 정리한 `DESIGN.md`를 받아, Claude Code 같은 AI 코딩 도구에 디자인 기준으로 줄 수 있습니다. `DESIGN.md`에는 색, 글꼴, 간격, 컴포넌트와 그렇게 정한 이유가 들어 있습니다.

1. [getdesign.md/design-md](https://getdesign.md/design-md) 목록에서 마음에 드는 디자인을 골라 `DESIGN.md` 내용을 복사합니다.
2. 저장소 루트에 `DESIGN.md` 파일로 저장합니다.
3. Claude Code에 이렇게 요청합니다.

   ```text
   DESIGN.md를 기준으로 블로그 디자인을 바꿔줘. UI를 고치기 전에 DESIGN.md를 먼저 읽어.
   ```

이 블로그의 디자인 값은 주로 아래 파일에 모여 있어서, 이 파일들부터 고치게 하면 됩니다.

| 무엇 | 위치 |
|---|---|
| 색, 글꼴 변수, 본문 폭과 여백 | `src/styles/global.css`의 `:root` |
| 글꼴 종류(Pretendard, Geist Mono) | `astro.config.mjs`의 `fonts` |
| 코드 블록 색 | `src/lib/shiki-theme.mjs` |
| 페이지별 배치 | `src/pages/`, `src/layouts/`의 `<style>` |

바꾼 뒤에는 `pnpm dev`로 데스크톱과 휴대폰 폭에서 화면을 확인하고, `pnpm build`가 통과하는지 봅니다.

> getdesign.md의 파일은 해당 회사가 공식으로 낸 디자인 시스템이 아닙니다. 사이트는 학습과 개발에 쓰는 출발점으로 소개하며, 상표와 디자인 요소의 권리는 각 소유자에게 있습니다. 특정 회사의 사이트처럼 보이도록 그대로 베끼기보다는 참고 자료로 쓰는 편이 안전합니다.

## Claude Code 스킬

저장소 폴더에서 [Claude Code](https://claude.com/claude-code)를 실행하면 `.claude/skills/`의 스킬을 바로 쓸 수 있습니다.

- **tech-blog-writing**: 한국어 기술 블로그 글을 기획 → 개요 → 섹션 → 마무리의 4단계 체크포인트로 나눠 쓰고, 단계마다 검토를 받습니다. 실행 출력·수치를 지어내지 않도록 근거 체크리스트로 점검합니다. "블로그 글 써줘", "이 글 검토해줘"처럼 말하면 시작합니다.
  - 초안은 `drafts/<slug>/`, 글의 원자료(노트북, 로그)는 `raw/<주제>/`에 둡니다. 두 폴더는 `.gitignore`에 들어 있어 커밋되지 않습니다.
  - 점검 규칙은 `docs/writing/`의 한국어 정오표(`korean-errata.md`)와 안티패턴(`anti-patterns.md`)에 있습니다. 정오표의 사례 표는 비어 있습니다. 글을 검토하며 고친 표현이 쌓이면 다음 글의 점검이 좋아집니다.
- **writing-rules-update**: 글을 고친 뒤 고친 표현과 리뷰에서 나온 새 유형 후보를 정오표·안티패턴에 반영합니다. 기존 유형의 사례인지, 새 유형인지, 고치지 않기로 한 결정인지 분류하고 확인을 받아 넣습니다. "이거 정오표에 추가해"처럼 말하면 시작합니다.
- **link-scrap**: URL을 주면 원문을 읽고 한국어 요약을 써서 스크랩 카드를 만듭니다. 코멘트(왜 골랐는지)는 직접 말해야 하고 지어내지 않습니다. "이 링크 스크랩해줘"처럼 말하면 시작합니다.

### Codex 스킬

[Codex](https://developers.openai.com/codex)를 쓴다면 `.agents/skills/`의 **review-technical-draft**로 원고를 리뷰할 수 있습니다. 원고는 고치지 않고, 코드·출력·설명이 맞는지와 한국어 표현을 점검한 리뷰 보고서(`<원고 이름>-review.md`)만 만듭니다. 정오표와 안티패턴은 Claude 스킬과 같은 `docs/writing/` 파일을 읽습니다.

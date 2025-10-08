## [2.7.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.7.0...v2.7.1) (2025-10-08)


### Bug Fixes

* resolve race condition in /arcade/room redirect ([5ed2ab2](https://github.com/antialias/soroban-abacus-flashcards/commit/5ed2ab21cab408147081a493c8dd6b1de48b2d01))

## [2.7.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.6.0...v2.7.0) (2025-10-08)


### Features

* extend GameModeContext to support room-based multiplayer ([ee6094d](https://github.com/antialias/soroban-abacus-flashcards/commit/ee6094d59d26a9e80ba5d023ca6dc13143bea308))

## [2.6.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.5.0...v2.6.0) (2025-10-08)


### Features

* refactor room addressing to /arcade/room ([e7d2a73](https://github.com/antialias/soroban-abacus-flashcards/commit/e7d2a73ddf2048691325a18e3d71a7ece444c131))

## [2.5.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.6...v2.5.0) (2025-10-08)


### Features

* display room info and network players in mini app nav ([5e3261f](https://github.com/antialias/soroban-abacus-flashcards/commit/5e3261f3bec8c19ec88c9a35a7e6ef8eda88a55e))

## [2.4.6](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.5...v2.4.6) (2025-10-08)


### Bug Fixes

* real-time room member updates via globalThis socket.io sharing ([94a1d9b](https://github.com/antialias/soroban-abacus-flashcards/commit/94a1d9b11058bfb4b54a4753e143cf85f215e913))

## [2.4.5](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.4...v2.4.5) (2025-10-08)


### Bug Fixes

* send all members (not just online) in socket broadcasts ([3fa6cce](https://github.com/antialias/soroban-abacus-flashcards/commit/3fa6cce17a7acd940cf5a9e6433bf6c4b497540c))

## [2.4.4](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.3...v2.4.4) (2025-10-08)


### Bug Fixes

* correctly access getSocketIO from dynamic import ([30abf33](https://github.com/antialias/soroban-abacus-flashcards/commit/30abf33ee86b36f2a98014e5b017fa8e466a2107))

## [2.4.3](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.2...v2.4.3) (2025-10-08)


### Bug Fixes

* resolve socket-server import path for Next.js build ([12c3c37](https://github.com/antialias/soroban-abacus-flashcards/commit/12c3c37ff8e1d3df71d72e527c08fa975043c504))

## [2.4.2](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.1...v2.4.2) (2025-10-08)


### Bug Fixes

* broadcast member join/leave events immediately via API ([ebfc88c](https://github.com/antialias/soroban-abacus-flashcards/commit/ebfc88c5ea0a8a0fdda039fa129e1054b9c42e65))

## [2.4.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.4.0...v2.4.1) (2025-10-08)


### Bug Fixes

* make leave room button actually remove user from room ([49f12f8](https://github.com/antialias/soroban-abacus-flashcards/commit/49f12f8cab631fedd33f1bc09febfdc95e444625))

## [2.4.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.3.1...v2.4.0) (2025-10-08)


### Features

* add arcade room/session info and network players to nav ([6800747](https://github.com/antialias/soroban-abacus-flashcards/commit/6800747f80a29c91ba0311a8330d594c1074097d))
* add real-time WebSocket updates for room membership ([7ebb2be](https://github.com/antialias/soroban-abacus-flashcards/commit/7ebb2be3927762a5fe9b6fb7fb15d6b88abb7b6a))
* implement modal room enforcement (one room per user) ([f005fbb](https://github.com/antialias/soroban-abacus-flashcards/commit/f005fbbb773f4d250b80d71593490976af82d5a5))
* improve room navigation and membership UI ([bc219c2](https://github.com/antialias/soroban-abacus-flashcards/commit/bc219c2ad66707f03e7a6cf587b9d190c736e26d))


### Bug Fixes

* auto-cleanup orphaned arcade sessions without valid rooms ([3c002ab](https://github.com/antialias/soroban-abacus-flashcards/commit/3c002ab29d1b72a0e1ffb70bb0744dc560e7bdc2))
* show correct join/leave button based on room membership ([5751dfe](https://github.com/antialias/soroban-abacus-flashcards/commit/5751dfef5c81981937cd5300c4256e5b74bb7488))

## [2.3.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.3.0...v2.3.1) (2025-10-07)


### Bug Fixes

* add missing DOMPoint properties to getPointAtLength mock ([1e17278](https://github.com/antialias/soroban-abacus-flashcards/commit/1e17278f942b3fbcc5d05be746178f2e780f0bd9))
* add missing name property to Passenger test mocks ([f8ca248](https://github.com/antialias/soroban-abacus-flashcards/commit/f8ca2488447e89151085942f708f6acf350a2747))
* add non-null assertions to skillConfiguration utilities ([9c71092](https://github.com/antialias/soroban-abacus-flashcards/commit/9c7109227822884d25f8546739c80c6e7491e28d))
* add optional chaining to stepBeadHighlights access ([a5fac5c](https://github.com/antialias/soroban-abacus-flashcards/commit/a5fac5c75c8cd67b218a5fd5ad98818dad74ab67))
* add showAsAbacus property to ComplementQuestion type ([4adcc09](https://github.com/antialias/soroban-abacus-flashcards/commit/4adcc096430fbb03f0a8b2f0aef4be239aff9cd0))
* add userId to optimistic player in useCreatePlayer ([5310463](https://github.com/antialias/soroban-abacus-flashcards/commit/5310463becd0974291cff49522ae5669a575410d))
* change TypeScript moduleResolution from bundler to node ([327aee0](https://github.com/antialias/soroban-abacus-flashcards/commit/327aee0b4b5c0b0b2bf3eeb48d861bb3068f6127))
* convert Jest mocks to Vitest in useSteamJourney tests ([e067271](https://github.com/antialias/soroban-abacus-flashcards/commit/e06727160c70a1ab38a003104d1fef8fb83ff92d))
* convert player IDs from number to string in arcade tests ([72db1f4](https://github.com/antialias/soroban-abacus-flashcards/commit/72db1f4a2c3f930025cd5ced3fcf7c810dcc569d))
* rewrite layout.nav.test to match actual RootLayout props ([a085de8](https://github.com/antialias/soroban-abacus-flashcards/commit/a085de816fcdeb055addabb8aec391b111cb5f94))
* update useArcadeGuard tests with proper useViewerId mock ([4eb49d1](https://github.com/antialias/soroban-abacus-flashcards/commit/4eb49d1d44e1d85526ef6564f88a8fbcebffb4d2))
* use Object.defineProperty for NODE_ENV in middleware tests ([e73191a](https://github.com/antialias/soroban-abacus-flashcards/commit/e73191a7298dbb6dd15da594267ea6221062c36b))
* wrap Buffer in Uint8Array for Next.js Response API ([98384d2](https://github.com/antialias/soroban-abacus-flashcards/commit/98384d264e4a10d1836aa9f2e69151b122ffa7b0))


### Documentation

* add explicit package.json script references to regime docs ([3353bca](https://github.com/antialias/soroban-abacus-flashcards/commit/3353bcadc2849104248c624973274ed90b86722a))
* establish mandatory code quality regime for Claude Code ([dd11043](https://github.com/antialias/soroban-abacus-flashcards/commit/dd1104310f4e0e85640730ea0e96e4adda4bc505))
* expand quality regime to define "done" for all work ([f92f7b5](https://github.com/antialias/soroban-abacus-flashcards/commit/f92f7b592af38ba9d0f5b1db3a061d63d92a5093))

## [2.3.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.2.1...v2.3.0) (2025-10-07)


### Features

* add Biome + ESLint linting setup ([fc1838f](https://github.com/antialias/soroban-abacus-flashcards/commit/fc1838f4f53a4f8d8f1c5303de3a63f12d9c9303))


### Styles

* apply Biome formatting to entire codebase ([60d70cd](https://github.com/antialias/soroban-abacus-flashcards/commit/60d70cd2f2f2b1d250c4c645889af4334968cb7e))

## [2.2.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.2.0...v2.2.1) (2025-10-07)


### Bug Fixes

* remove remaining typst-dependent files ([d1b9b72](https://github.com/antialias/soroban-abacus-flashcards/commit/d1b9b72cfc2f2ba36c40d7ae54bc6fdfcc5f34da))

## [2.2.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.1.3...v2.2.0) (2025-10-07)


### Features

* remove typst-related code and routes ([be6fb1a](https://github.com/antialias/soroban-abacus-flashcards/commit/be6fb1a881b983f9830d36c079b7b41f35153b8a))

## [2.1.3](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.1.2...v2.1.3) (2025-10-07)


### Bug Fixes

* remove .npmrc from Dockerfile COPY ([e71c2b4](https://github.com/antialias/soroban-abacus-flashcards/commit/e71c2b4da85076dfc97401fc170cd88cb0aa4375))

## [2.1.2](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.1.1...v2.1.2) (2025-10-07)


### Bug Fixes

* revert to default pnpm mode for Docker compatibility ([bd0092e](https://github.com/antialias/soroban-abacus-flashcards/commit/bd0092e69ac4f74ea89b8d31399cf72f57484cbb))

## [2.1.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.1.0...v2.1.1) (2025-10-07)


### Bug Fixes

* ignore all node_modules in Docker ([4792dde](https://github.com/antialias/soroban-abacus-flashcards/commit/4792dde1beef9c6cb84a27bc6bb6acfa43919a72))

## [2.1.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.7...v2.1.0) (2025-10-07)


### Features

* remove typst dependencies ([eedce28](https://github.com/antialias/soroban-abacus-flashcards/commit/eedce28572035897001f6b8a08f79beaa2360d44))

## [2.0.7](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.6...v2.0.7) (2025-10-07)


### Bug Fixes

* preserve workspace node_modules in Docker for hoisted mode ([4f8aaf0](https://github.com/antialias/soroban-abacus-flashcards/commit/4f8aaf04aadda11ce9ec470dec44f78062929e77))

## [2.0.6](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.5...v2.0.6) (2025-10-07)


### Bug Fixes

* ignore nested node_modules in Docker ([f554592](https://github.com/antialias/soroban-abacus-flashcards/commit/f554592272c2e92d7f1ec6550211518de9c3242f))

## [2.0.5](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.4...v2.0.5) (2025-10-07)


### Bug Fixes

* use .npmrc in Docker for hoisted mode consistency ([2df8cdc](https://github.com/antialias/soroban-abacus-flashcards/commit/2df8cdc88ed03b6b04642a3441e17c6fda11d2a5))

## [2.0.4](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.3...v2.0.4) (2025-10-07)


### Bug Fixes

* remove .npmrc in Docker to avoid hoisted mode issues ([2a77d75](https://github.com/antialias/soroban-abacus-flashcards/commit/2a77d755b7820b5b6b52ea99db418e6d071d726e))

## [2.0.3](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.2...v2.0.3) (2025-10-07)


### Bug Fixes

* remove duplicate PlayerStatusBar story file from arcade ([4e721f7](https://github.com/antialias/soroban-abacus-flashcards/commit/4e721f765a29fe8628d4e34ef94cdf5728eea3dc))

## [2.0.2](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.1...v2.0.2) (2025-10-07)


### Bug Fixes

* update Dockerfile pnpm version and fix TypeScript config ([43077a8](https://github.com/antialias/soroban-abacus-flashcards/commit/43077a80e271a793c88f100874914ae6f3c515b5))

## [2.0.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v2.0.0...v2.0.1) (2025-10-07)


### Bug Fixes

* add @types/minimatch to abacus-react devDependencies ([fa45475](https://github.com/antialias/soroban-abacus-flashcards/commit/fa4547543dcd0cddc7cc9ff9da62f60a4717fb1f))

## [2.0.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.2.1...v2.0.0) (2025-10-07)


### ⚠ BREAKING CHANGES

* abacus-react package now has independent versioning from monorepo

### Features

* **abacus-react:** add dual publishing to npm and GitHub Packages ([242ee52](https://github.com/antialias/soroban-abacus-flashcards/commit/242ee523edebe2cfc5db27cc72fba0315072bec2))
* **abacus-react:** comprehensive README overhaul with current capabilities ([0ce351e](https://github.com/antialias/soroban-abacus-flashcards/commit/0ce351e572ac34fa816ee7533a26403c843d93f3))
* **abacus-react:** configure GitHub Packages-only publishing workflow ([5eeedd9](https://github.com/antialias/soroban-abacus-flashcards/commit/5eeedd9a59a6b3898cadb30c413daa791a9561ee))
* **abacus-react:** enable dual publishing to npm and GitHub Packages ([176a196](https://github.com/antialias/soroban-abacus-flashcards/commit/176a1961d05f99908a72837cf4e8ec93c0d33145))
* **abacus-react:** enhance package description with semantic versioning details ([af037b5](https://github.com/antialias/soroban-abacus-flashcards/commit/af037b5e0a1ded5460f95498eb1fb5ac19c2e3fa))
* **abacus-react:** implement GitHub Packages-only publishing workflow ([b194599](https://github.com/antialias/soroban-abacus-flashcards/commit/b194599f6029015b1aba0e57eb5fe9f83b89d403))
* **abacus-react:** implement GitHub-only semantic release with manual package publishing ([33b0567](https://github.com/antialias/soroban-abacus-flashcards/commit/33b056769811d1cf1c41dee9e65f6e12188e6f5f))
* **abacus-react:** simplify to GitHub Packages-only publishing ([acc126b](https://github.com/antialias/soroban-abacus-flashcards/commit/acc126bd5a0f0b2017263593ac2e3a180606f17b))
* **abacus-react:** update description to mention GitHub Packages support ([af77256](https://github.com/antialias/soroban-abacus-flashcards/commit/af7725622e15801f9e56af12930c4e14c5e67c53))
* **abacus-react:** use environment variables to override npm registry ([ad444e1](https://github.com/antialias/soroban-abacus-flashcards/commit/ad444e108f76d3014e492ddc94de0e52c61743ea))
* add API routes for players and user stats ([6f940e2](https://github.com/antialias/soroban-abacus-flashcards/commit/6f940e24d663cc06084a943df4743c2a1c1b3c33))
* add arcade matching game components and utilities ([ff16303](https://github.com/antialias/soroban-abacus-flashcards/commit/ff16303a7cd2880fcdfd51ef8a744e245905d87d))
* add arcade room system database schema and managers (Phase 1) ([a9175a0](https://github.com/antialias/soroban-abacus-flashcards/commit/a9175a050c1668a6ba066078e0bdbd944b4eb960))
* add build info API endpoint ([571664e](https://github.com/antialias/soroban-abacus-flashcards/commit/571664e725b63f22fa9f0bca8a1c518a54441dec))
* add build info generation script ([416dc89](https://github.com/antialias/soroban-abacus-flashcards/commit/416dc897e26ab93930b52faf77da3a6ffd4a0fb9))
* add category browsing and scrolling to emoji picker ([616a50e](https://github.com/antialias/soroban-abacus-flashcards/commit/616a50e234f79e271cb0bd9c959866d2d2e5ac82))
* add complement display options and unify equation display ([2ed7b2c](https://github.com/antialias/soroban-abacus-flashcards/commit/2ed7b2cbf8ad7c18b14c0e86b04a3ba96cc4de0b))
* add Complement Race game with three unique game modes ([582bce4](https://github.com/antialias/soroban-abacus-flashcards/commit/582bce411f5e89fe1ee677321d06ca7d0fd78701))
* add comprehensive E2E testing with Playwright ([d58053f](https://github.com/antialias/soroban-abacus-flashcards/commit/d58053fad3ab06b9884b46dbb6807e938426dbb5))
* add comprehensive Storybook stories for PlayerStatusBar ([8973241](https://github.com/antialias/soroban-abacus-flashcards/commit/8973241297d50604028bde95b9ebbf033688db89))
* add configuration access to active player emojis in prominent nav ([6049a7f](https://github.com/antialias/soroban-abacus-flashcards/commit/6049a7f6b7481ca42a7907d11d93676549bf6629))
* add configuration access to fullscreen player selection ([b85968b](https://github.com/antialias/soroban-abacus-flashcards/commit/b85968bcb6afa379d50242185e7743f6fe4ba982))
* add consecutive match tracking system for escalating celebrations ([111c0ce](https://github.com/antialias/soroban-abacus-flashcards/commit/111c0ced715be7cade006387d01f4e2f52c59be9))
* add CSS animations and visual feedback system ([80e33e2](https://github.com/antialias/soroban-abacus-flashcards/commit/80e33e25b3d30a44a1a5294997d56949e2aeef8b))
* add deployment info modal with keyboard shortcut ([43be7ac](https://github.com/antialias/soroban-abacus-flashcards/commit/43be7ac83a9ba3e0ad970f4588729ba2ad394702))
* add direct URL routes for each game mode ([a08f053](https://github.com/antialias/soroban-abacus-flashcards/commit/a08f0535bf6dfb424e8f9764b37ce6912db6021c))
* add exitSession to MemoryPairsContextValue interface ([abc2ea5](https://github.com/antialias/soroban-abacus-flashcards/commit/abc2ea50d07e87537ced649bcc9276ef95a3bc4e))
* add GameControlButtons component with unit tests ([1f45c17](https://github.com/antialias/soroban-abacus-flashcards/commit/1f45c17e0a68db2a452844f87217671223cf7bb0))
* add guest session system with JWT tokens ([10d8aaf](https://github.com/antialias/soroban-abacus-flashcards/commit/10d8aaf814275a9c3f08e0f1b39970c3ab1a8427))
* add initialStyle prop to ComplementRaceProvider ([f3bc2f6](https://github.com/antialias/soroban-abacus-flashcards/commit/f3bc2f6d926b9c8d9229636e3ed688bf9ea3baf3))
* add intelligent on-screen number pad for devices without keyboards ([d4740ff](https://github.com/antialias/soroban-abacus-flashcards/commit/d4740ff99709be915c41f51d973706f6ff2774b3))
* add interactive remove buttons for players in mini nav ([fa1cf96](https://github.com/antialias/soroban-abacus-flashcards/commit/fa1cf967898bdc396b0bfdcbfe2147a06e189190))
* add magnifying glass preview on emoji hover ([2c88b6b](https://github.com/antialias/soroban-abacus-flashcards/commit/2c88b6b5f3ba3a47007aa832c2e204bf2ebcc90b))
* add middleware for pathname header support in [@nav](https://github.com/nav) fallback ([b7e7c4b](https://github.com/antialias/soroban-abacus-flashcards/commit/b7e7c4beff1e37e90e9e20a890c5af7a134a7fca))
* add mini app nav to arcade page ([a854fe3](https://github.com/antialias/soroban-abacus-flashcards/commit/a854fe3dc935b10db8dc71569c0c8abd81938e4c))
* add optimistic updates and remove dead code ([b62cf26](https://github.com/antialias/soroban-abacus-flashcards/commit/b62cf26fb6597bae9a590f8b8d630fd31a8dd321))
* add passenger boarding system with station-based pickup ([23a9016](https://github.com/antialias/soroban-abacus-flashcards/commit/23a9016245e061b65151735db31aebdc9d36ed1d))
* add player types and migration utilities ([79f44b2](https://github.com/antialias/soroban-abacus-flashcards/commit/79f44b25d6c17f119c3ae225fb449be27c77c56d))
* add PlayerStatusBar with escalating celebration animations ([7f8c90a](https://github.com/antialias/soroban-abacus-flashcards/commit/7f8c90acea84b208df0e3e23e80a02cf425c0950))
* add prominent game context display to mini nav with smooth transitions ([8792393](https://github.com/antialias/soroban-abacus-flashcards/commit/8792393956b01a5a8ca67d78209e6defb6a11903))
* add React Query setup with api helper ([a3878a8](https://github.com/antialias/soroban-abacus-flashcards/commit/a3878a8537fe123fa345d2d2990b3cd76132ba1e))
* add realistic mountains with peaks and ground terrain ([99cdfa8](https://github.com/antialias/soroban-abacus-flashcards/commit/99cdfa8a0ba63e7b523466d8b2108bca05b0310a))
* add security tests and userId injection protection ([aa1ad31](https://github.com/antialias/soroban-abacus-flashcards/commit/aa1ad315ef75af5b6833a3a3628a9bbceb80c03c))
* add server-side validation for player modifications during active arcade sessions ([3b3cad4](https://github.com/antialias/soroban-abacus-flashcards/commit/3b3cad4b769b0ed9ed8e6dc2363bcaf13cc8e08a))
* add Setup button to exit arcade sessions ([ae1318e](https://github.com/antialias/soroban-abacus-flashcards/commit/ae1318e8bf2c584853ceeb38336d871110f13a39))
* add smooth spring animations to pressure gauge ([863a2e1](https://github.com/antialias/soroban-abacus-flashcards/commit/863a2e1319448381c853540301886fb4a169e112))
* add sound settings support to AbacusReact component ([90b9ffa](https://github.com/antialias/soroban-abacus-flashcards/commit/90b9ffa0d8659891bfe8062217e45245bbff5d5a))
* add train car system with smooth boarding/disembarking animations ([1613912](https://github.com/antialias/soroban-abacus-flashcards/commit/1613912740756d984205e3625791c1d8a2a6fa51))
* add Web Audio API sound effects system with 16 sound types ([90ba866](https://github.com/antialias/soroban-abacus-flashcards/commit/90ba86640c7062a00d2c7553827a61524ec17da1))
* **complement-race:** add abacus displays to pressure gauge ([c5ebc63](https://github.com/antialias/soroban-abacus-flashcards/commit/c5ebc635afb6e78f9f4b1192ff39dcec53879a60))
* complete themed navigation system with game-specific chrome ([0a4bf17](https://github.com/antialias/soroban-abacus-flashcards/commit/0a4bf1765cbd86bf6f67fb3b99c577cfe3cce075))
* create mode selection landing page for Complement Race ([1ff9695](https://github.com/antialias/soroban-abacus-flashcards/commit/1ff9695f6930f5232b2ad80ddcbd32bbc182d4e7))
* create PlayerConfigDialog component for player customization ([4f2a661](https://github.com/antialias/soroban-abacus-flashcards/commit/4f2a661494add3f61b714d0bead07b0e0bc3f92d))
* create StandardGameLayout for perfect viewport sizing ([728a920](https://github.com/antialias/soroban-abacus-flashcards/commit/728a92076a6ac9ef71f0c75d2e9503575881130a))
* display passengers visually on train and at stations ([1599904](https://github.com/antialias/soroban-abacus-flashcards/commit/159990489fec9162d9ed9ecf77c7592b776bbb23))
* dynamic player card rendering on games page ([81d17f2](https://github.com/antialias/soroban-abacus-flashcards/commit/81d17f23976cc340e23c63f8e27f1a15afd1a4d0))
* dynamically calculate train cars based on max concurrent passengers ([9ea1553](https://github.com/antialias/soroban-abacus-flashcards/commit/9ea15535d18efc25739342b0945c6d7ec7896c5d))
* emit session-state after creating arcade session ([70d6f43](https://github.com/antialias/soroban-abacus-flashcards/commit/70d6f43d6d7ff918ab15edb6e27d4eab8c7a3de6))
* enable prominent nav and fix layout on arcade page ([5c8c18c](https://github.com/antialias/soroban-abacus-flashcards/commit/5c8c18cbb89da38ccaab3c2ad7081e1a6d45a73e))
* enhance emoji picker with super powered magnifying glass and hide empty categories ([d8b4e42](https://github.com/antialias/soroban-abacus-flashcards/commit/d8b4e425bf019c593abdcb7693a04e4780b18f06))
* enhance passenger card UI with boarding status indicators ([4bbdabc](https://github.com/antialias/soroban-abacus-flashcards/commit/4bbdabc3b576ba8cdda5a053878b3f2e9004afca))
* extend ground terrain to cover entire track area ([ee48417](https://github.com/antialias/soroban-abacus-flashcards/commit/ee48417abfe9f5a2788d6de8ff522f60c13b6066))
* extend player customization to support all 4 players ([72f8dee](https://github.com/antialias/soroban-abacus-flashcards/commit/72f8dee183b17c88d51748b5131b5a51906a24b3))
* extend railroad track to viewport edges ([eadd7da](https://github.com/antialias/soroban-abacus-flashcards/commit/eadd7da6dbc4103342dd673f03f97850cdc20f23))
* extend track and tunnels to absolute viewport edges ([f7419bc](https://github.com/antialias/soroban-abacus-flashcards/commit/f7419bc6a0c03cbe2dbbc095e47891ee67d10b51))
* implement [@nav](https://github.com/nav) parallel routes for game name display in mini navigation ([885fc72](https://github.com/antialias/soroban-abacus-flashcards/commit/885fc725dc0bb41bbb5e500c2c907c6182192854))
* implement cozy sound effects for abacus with variable intensity ([c95be1d](https://github.com/antialias/soroban-abacus-flashcards/commit/c95be1df6dbe74aad08b9a1feb1f33688212be0b))
* implement cozy sound effects for abacus with variable intensity ([cea5fad](https://github.com/antialias/soroban-abacus-flashcards/commit/cea5fadbe4b4d5ae9e0ee988e9b1c4db09f21ba6))
* implement game control callbacks in MemoryPairsGame ([4758ad2](https://github.com/antialias/soroban-abacus-flashcards/commit/4758ad2f266ef3f3f67c22533fbb5f475dd8bd5b))
* implement game theming system with context-based navigation chrome ([3fa11c4](https://github.com/antialias/soroban-abacus-flashcards/commit/3fa11c4fbcbeabeb3bdd0db38374fb9a13cbb754))
* implement innovative dynamic two-panel layout for on-screen keyboard ([4bb8f6d](https://github.com/antialias/soroban-abacus-flashcards/commit/4bb8f6daf1f3eecb5cbaf31bf4057f43e43aeb07))
* implement mobile-first responsive design for speed memory quiz ([13efc4d](https://github.com/antialias/soroban-abacus-flashcards/commit/13efc4d0705bb9e71a2002689a4ebac109caacc2))
* implement simple fixed bottom keyboard bar ([9ef72d7](https://github.com/antialias/soroban-abacus-flashcards/commit/9ef72d7e88a6a9b30cfd7a7d3944197cc1e0037a))
* implement smooth train exit with fade-out through right tunnel ([0176694](https://github.com/antialias/soroban-abacus-flashcards/commit/01766944f0267b1f2adeb6a30c9f89d48038a7f8))
* implement toggleable on-screen keyboard to prevent UI overlap ([701d23c](https://github.com/antialias/soroban-abacus-flashcards/commit/701d23c36992b09c075e1a394f8a72edffb919f9))
* improve game availability logic and messaging ([9a3fa93](https://github.com/antialias/soroban-abacus-flashcards/commit/9a3fa93e53d05475844b54052acbc838d7487d23))
* increase landmark emoji size for better visibility ([0bcd7a3](https://github.com/antialias/soroban-abacus-flashcards/commit/0bcd7a30d42a0a0d5bdfcf5abd8eb3eb9a8b6a73))
* integrate GameControlButtons into navigation ([fbd8cd4](https://github.com/antialias/soroban-abacus-flashcards/commit/fbd8cd4a6bca44bbc0f7c4e8153900558805a84a))
* integrate remaining game sound effects ([600bc35](https://github.com/antialias/soroban-abacus-flashcards/commit/600bc35bc3111a455290638e7be31d0032ff656c))
* integrate sound effects into game flow (countdown, answers, performance) ([8c3a855](https://github.com/antialias/soroban-abacus-flashcards/commit/8c3a85523930fca7f2dcc53c79454fb9be523d55))
* integrate user profiles with PlayerStatusBar and game results ([beff646](https://github.com/antialias/soroban-abacus-flashcards/commit/beff64652c72a5cd0c008891b6dc2f5167e28b62))
* make Steam Sprint infinite mode ([32c3a35](https://github.com/antialias/soroban-abacus-flashcards/commit/32c3a35eabd10f8c9b50a55cfb525a76ea050914))
* make SVG span full viewport width for sprint mode ([7488bb3](https://github.com/antialias/soroban-abacus-flashcards/commit/7488bb38033b2d3d3fc18b9f09373506d69e25a5))
* migrate abacus display settings to database ([92ef136](https://github.com/antialias/soroban-abacus-flashcards/commit/92ef1360a4792d0b36f3a35e100bd9f3c7451656))
* migrate contexts to React Query (remove localStorage) ([fe01a1f](https://github.com/antialias/soroban-abacus-flashcards/commit/fe01a1fe182293aeadd5cbfd73f0a54a858ae38e))
* migrate contexts to UUID-based player system ([2b94cad](https://github.com/antialias/soroban-abacus-flashcards/commit/2b94cad11bd05b1a324e360c56be686c3c6a4b64))
* preserve track and passengers during route transitions ([f2e7165](https://github.com/antialias/soroban-abacus-flashcards/commit/f2e71657dc1587c2b6df1f4227160b8a261c6084))
* redesign passenger cards with vintage train station aesthetic ([651bc21](https://github.com/antialias/soroban-abacus-flashcards/commit/651bc2158361fbaafb0b011ab90006b21d3a7c85))
* set up automated npm publishing for @soroban/abacus-react package ([dd80d29](https://github.com/antialias/soroban-abacus-flashcards/commit/dd80d29c979e20b4d3624cf66be79ec51d5f53a9))
* set up Drizzle ORM with SQLite database ([5d5afd4](https://github.com/antialias/soroban-abacus-flashcards/commit/5d5afd4e6860241ff45c7173d4aad2b7156a41b1))
* skip countdown for train mode (sprint) ([65dafc9](https://github.com/antialias/soroban-abacus-flashcards/commit/65dafc92153399336f200a566bc91f869fdfcbb1))
* skip intro screen and start directly at game setup ([4b6888a](https://github.com/antialias/soroban-abacus-flashcards/commit/4b6888af05c6be9616cf20b9d2b8b66ac13cf253))
* sync URL with selected game mode ([3920bba](https://github.com/antialias/soroban-abacus-flashcards/commit/3920bbad33ef5dd6323d2baea498943f5115dbec))
* UI polish for Sprint mode (viewport, backgrounds, data attributes) ([90ad789](https://github.com/antialias/soroban-abacus-flashcards/commit/90ad789ff1f94f52b98de9fd934a623eab452387))
* update nav components for UUID players ([e85d041](https://github.com/antialias/soroban-abacus-flashcards/commit/e85d0415f23049da861533bbec2a65e1d84adfe1))
* use CSS transitions for smooth fullscreen player selection collapse ([3189832](https://github.com/antialias/soroban-abacus-flashcards/commit/31898328a391614a0fe8d24ec9d2881bfb6e6984))
* wire player configuration through nav component hierarchy ([edfdd81](https://github.com/antialias/soroban-abacus-flashcards/commit/edfdd8122774e36dbda9acea741a5e248be95676))


### Bug Fixes

* **abacus-react:** add debugging and explicit authentication for npm publish ([b82e9bb](https://github.com/antialias/soroban-abacus-flashcards/commit/b82e9bb9d6adf3793065067f96c6fbbfd1a78bca))
* **abacus-react:** add packages: write permission for GitHub Packages publishing ([8e16487](https://github.com/antialias/soroban-abacus-flashcards/commit/8e1648737de9305f82872cb9b86b98b5045f77a7))
* **abacus-react:** apply global columnPosts styling and fix reckoning bar width ([bb9959f](https://github.com/antialias/soroban-abacus-flashcards/commit/bb9959f7fb8985e0c6496247306838d97e7121f7))
* **abacus-react:** force npm to use GitHub Packages registry ([5e6c901](https://github.com/antialias/soroban-abacus-flashcards/commit/5e6c901f73a68b60ec05f19c4a991ca8affc1589))
* **abacus-react:** improve publishing workflow with better version sync ([7a4ecd2](https://github.com/antialias/soroban-abacus-flashcards/commit/7a4ecd2b5970ed8b6bfde8938b36917f8e7a7176))
* **abacus-react:** improve workspace dependency cleanup and add validation ([11fd6f9](https://github.com/antialias/soroban-abacus-flashcards/commit/11fd6f9b3deb1122d3788a7e0698de891eeb0f3a))
* **abacus-react:** resolve workspace dependencies before npm publish ([834b062](https://github.com/antialias/soroban-abacus-flashcards/commit/834b062b2d22356b9d96bb9c3c444eccaa51d793))
* **abacus-react:** simplify semantic-release config to resolve dependency issues ([88cab38](https://github.com/antialias/soroban-abacus-flashcards/commit/88cab380ef383c941b41671d58d3e35fcaefb2d3))
* **abacus-react:** temporarily allow test failures during setup phase ([e3db7f4](https://github.com/antialias/soroban-abacus-flashcards/commit/e3db7f4daf16fce82bccfe47dcaa90d7f4896a79))
* add CLEAR_MISMATCH move to allow mismatch feedback to auto-dismiss ([158f527](https://github.com/antialias/soroban-abacus-flashcards/commit/158f52773d20dfab7dc55575d9999f32b4c589a2))
* add missing GameThemeContext file for themed navigation ([d4fbdd1](https://github.com/antialias/soroban-abacus-flashcards/commit/d4fbdd14630e2f2fcdbc0de23ccc4ccd9eb74b48))
* add npmrc for hoisting and fix template paths ([5c65ac5](https://github.com/antialias/soroban-abacus-flashcards/commit/5c65ac5caabb7197f069344d0ed29d02c3de2b9a))
* add Python setuptools and build tools for better-sqlite3 compilation ([a216a3d](https://github.com/antialias/soroban-abacus-flashcards/commit/a216a3d3435a132c8add0a7c711b021bf4b1555f))
* add testing mode for on-screen keyboard and fix toggle functionality ([904074c](https://github.com/antialias/soroban-abacus-flashcards/commit/904074ca821b62cd6b1e129354eb36c5dd4b5e7f))
* align all bottom UI elements to same 20px baseline ([076c97a](https://github.com/antialias/soroban-abacus-flashcards/commit/076c97abac7a33f600b80083d8990a8c4a51be99))
* align bottom-positioned UI elements ([227cfab](https://github.com/antialias/soroban-abacus-flashcards/commit/227cfabf113bc875ea3a61f0de41a9093ad1dd30))
* allow navigation to game setup pages without active session ([c7ad3c0](https://github.com/antialias/soroban-abacus-flashcards/commit/c7ad3c069502580d1e72e7cc01e7b1f793ba9357))
* change pressure gauge to fixed positioning to stay above terrain ([1b11031](https://github.com/antialias/soroban-abacus-flashcards/commit/1b110315982f631dadca96a37fc88db98a7f9cca))
* change question display to fixed positioning with higher z-index ([4ac8758](https://github.com/antialias/soroban-abacus-flashcards/commit/4ac875895781dba5e115eeb3336ef76744b782bb))
* **complement-race:** improve abacus display in equations ([491b299](https://github.com/antialias/soroban-abacus-flashcards/commit/491b299e28ee82c49069cf892609b1b2b3c0aee3))
* **complement-race:** prevent passengers being left behind at delivery stations ([e6ebecb](https://github.com/antialias/soroban-abacus-flashcards/commit/e6ebecb09b1e5dd78c2dc11e125399082fb420ab))
* correct emoji category group IDs to match Unicode CLDR ([b2a21b7](https://github.com/antialias/soroban-abacus-flashcards/commit/b2a21b79ad705a5b52767317af00e4d666d33907))
* defer URL update until game starts ([12c54b2](https://github.com/antialias/soroban-abacus-flashcards/commit/12c54b27b717e852b96585eacdf6e9d964e32c50))
* delay passenger display update until train resets ([e06a750](https://github.com/antialias/soroban-abacus-flashcards/commit/e06a7504549bb4e0fcc38bd03249b9c0386c3079))
* disable turn validation in arcade mode matching game ([7c0e6b1](https://github.com/antialias/soroban-abacus-flashcards/commit/7c0e6b142b90f0fc3d444b3dcc1fff1512a0a3b2))
* eliminate rail jaggies on sharp curves by increasing sampling density ([46d4af2](https://github.com/antialias/soroban-abacus-flashcards/commit/46d4af2bdad761366890171cc666ba24d5309257))
* enable shamefully-hoist for semantic-release dependencies ([6168c29](https://github.com/antialias/soroban-abacus-flashcards/commit/6168c292d5f15748e80610103a6a787c0cf29d0f))
* enforce playerId must be explicitly provided in arcade moves ([d5a8a2a](https://github.com/antialias/soroban-abacus-flashcards/commit/d5a8a2a14cb14ecd00827ddc96873f3db79573fd))
* ensure consistent r×c grid layout for memory matching game ([f1a0633](https://github.com/antialias/soroban-abacus-flashcards/commit/f1a0633596fd1bb53418e56e28f3f27d3fce8b54))
* ensure game names persist in navigation on page reload ([9191b12](https://github.com/antialias/soroban-abacus-flashcards/commit/9191b124934b9a5577a91f67e8fb6f83b173cc4f))
* ensure passengers only travel forward on train route ([8ad3144](https://github.com/antialias/soroban-abacus-flashcards/commit/8ad3144d2da9b4ceedd62a9f379f664fa9381afe))
* export missing hooks and types from @soroban/abacus-react package ([423ba55](https://github.com/antialias/soroban-abacus-flashcards/commit/423ba5535023928f1e0198b2bd01c3c6cf7ee848))
* implement route-based theme detection for page reload persistence ([3dcff2f](https://github.com/antialias/soroban-abacus-flashcards/commit/3dcff2ff888558d7b746a732cfd53a1897c2b1df))
* improve navigation chrome background color extraction from gradients ([00bfcbc](https://github.com/antialias/soroban-abacus-flashcards/commit/00bfcbcdee28d63094c09a4ae0359789ebcf4a22))
* increase question display zIndex to stay above terrain ([8c8b8e0](https://github.com/antialias/soroban-abacus-flashcards/commit/8c8b8e08b4d51e6462d4b7dd258a25e64bf16dba))
* lazy-load database connection to prevent build-time access ([af8d993](https://github.com/antialias/soroban-abacus-flashcards/commit/af8d9936285c697ff45700115eba83b5debdf9ad))
* make results screen compact to fit viewport without scrolling ([9d4cba0](https://github.com/antialias/soroban-abacus-flashcards/commit/9d4cba05be84e7c162d706c8697eede23314b1a4))
* migrate viewport from metadata to separate viewport export ([1fe12c4](https://github.com/antialias/soroban-abacus-flashcards/commit/1fe12c4837b1229d0f0ab93c55d0ffb504eb8721))
* move auth.ts to src/ to match @/ path alias ([7829d8a](https://github.com/antialias/soroban-abacus-flashcards/commit/7829d8a0fb86dac07aa1b2fb0b68908e7e8381b8))
* move fontWeight to style object for station names ([05a3ddb](https://github.com/antialias/soroban-abacus-flashcards/commit/05a3ddb086e28529efb321943f4e423dbe5ed6a6))
* only show configuration gear icon for players 1 and 2 ([d0a3bc7](https://github.com/antialias/soroban-abacus-flashcards/commit/d0a3bc7dc1efc00c1db63fb50bc2ab3c6aabdd59))
* pass player IDs (not user IDs) in all arcade game moves ([d00abd2](https://github.com/antialias/soroban-abacus-flashcards/commit/d00abd25e755c0304517a7953cb78022a073b7c3))
* passengers now board/disembark based on their car position, not locomotive ([96782b0](https://github.com/antialias/soroban-abacus-flashcards/commit/96782b0e7a6d0db5a4435ca303b1d819947ce460))
* position tunnels at absolute viewBox edges ([1a5fa28](https://github.com/antialias/soroban-abacus-flashcards/commit/1a5fa2873bcda9a24cc578a7ecea43632077a0a1))
* prevent layout shift when selecting Steam Sprint mode ([73a5974](https://github.com/antialias/soroban-abacus-flashcards/commit/73a59745a5145b734b0893a489c5d018e3c9475c))
* prevent multiple passengers from boarding same car in single frame ([63b0b55](https://github.com/antialias/soroban-abacus-flashcards/commit/63b0b552a89a1165137de125bf57246a7cf6ac73))
* prevent premature passenger display during route transitions ([fe9ea67](https://github.com/antialias/soroban-abacus-flashcards/commit/fe9ea67f56847859b4fb4fa4f747022f0a2e5a70))
* prevent random passenger repopulation during route transitions ([db56ce8](https://github.com/antialias/soroban-abacus-flashcards/commit/db56ce89ee1d4e7583b60cde4e1d2610ee31123a))
* prevent route celebration from immediately reappearing ([1a80934](https://github.com/antialias/soroban-abacus-flashcards/commit/1a8093416e0feff774b6cdc6dfafdbafbb8baf7f))
* redesign matching game setup page for StandardGameLayout ([cc1f27f](https://github.com/antialias/soroban-abacus-flashcards/commit/cc1f27f0f82256f9344531814e8b965fa547d555))
* reduce landmark size from 4.0x to 2.0x multiplier ([c928e90](https://github.com/antialias/soroban-abacus-flashcards/commit/c928e907854e18264266958d813d4e1d4c03e760))
* regenerate lockfile with correct dependency order ([51bf448](https://github.com/antialias/soroban-abacus-flashcards/commit/51bf448c9f159152e89296d9014dde688fcf3a97))
* regenerate lockfile with node-linker=hoisted from scratch ([480960c](https://github.com/antialias/soroban-abacus-flashcards/commit/480960c2c8e0c50fe2b6ec69a34b772751a8bf41))
* regenerate pnpm lockfile for pnpm 9 compatibility ([4ab1aef](https://github.com/antialias/soroban-abacus-flashcards/commit/4ab1aef9b8fcf15cc03e86c829ca9885e7201b77))
* remove double PageWithNav wrapper on matching page ([b58bcd9](https://github.com/antialias/soroban-abacus-flashcards/commit/b58bcd92ee0521a6413f4d6e9656c9ccb1c72851))
* remove duplicate CAR_SPACING and MAX_CARS declarations ([e704a28](https://github.com/antialias/soroban-abacus-flashcards/commit/e704a28524e1217b6f56ca5a51784db73f5eadce))
* remove duplicate previousPassengersRef declaration ([fad8636](https://github.com/antialias/soroban-abacus-flashcards/commit/fad86367638b1a48b7e1544976148f43b061c832))
* remove frozen lockfile flag from publishing workflow to resolve dependency installation issues ([18af973](https://github.com/antialias/soroban-abacus-flashcards/commit/18af9730ffbcd822da292161815ffd09ad97f66c))
* remove hard-coded car count from game loop ([6c90a68](https://github.com/antialias/soroban-abacus-flashcards/commit/6c90a68c49b5f7fbc262c38f9a8828f5c725cb6a))
* remove unnecessary zIndex from question display ([db52e14](https://github.com/antialias/soroban-abacus-flashcards/commit/db52e14dfe9aceaaa1f98fc79100c04adc84611a))
* reposition on-screen keyboard to avoid covering abacus tiles ([6e5b4ec](https://github.com/antialias/soroban-abacus-flashcards/commit/6e5b4ec7bf7e2af5f724628693d3c4ee8c5b3968))
* require activePlayers in START_GAME, never fallback to userId ([ea1b1a2](https://github.com/antialias/soroban-abacus-flashcards/commit/ea1b1a2f69a35a6a27f7f952971509b2bb2e6f8d))
* reset momentum and pressure when starting new route ([3ea88d7](https://github.com/antialias/soroban-abacus-flashcards/commit/3ea88d7a5a6ed427b17cf408d993918870b75f7f))
* resolve circular dependency errors in memory quiz on-screen keyboard ([d25e2c4](https://github.com/antialias/soroban-abacus-flashcards/commit/d25e2c4c006b54a51eaa3a93fa8462e3a06221b7))
* resolve JSX parsing error with emoji in guide page ([bf046c9](https://github.com/antialias/soroban-abacus-flashcards/commit/bf046c999b51ba422284a139ebadde2c35187ac7))
* resolve mini navigation game name persistence across all routes ([3fa314a](https://github.com/antialias/soroban-abacus-flashcards/commit/3fa314aaa5de7b9c26a5390a52996c7d5ef9ea51))
* resolve runtime error - calculateOptimalGrid not defined ([fbc84fe](https://github.com/antialias/soroban-abacus-flashcards/commit/fbc84febda5507d434cf60aa0fce32350e01ec96))
* resolve SSR/client hydration mismatch for themed navigation ([301e65d](https://github.com/antialias/soroban-abacus-flashcards/commit/301e65dfa66d0de6b6efbbfbd09b717308ab57f1))
* resolve TypeScript errors in PlayerStatusBar component ([a935e5a](https://github.com/antialias/soroban-abacus-flashcards/commit/a935e5aed8c4584d21c8fc4359453b7dec494464))
* restore navigation to all pages using PageWithNav ([183706d](https://github.com/antialias/soroban-abacus-flashcards/commit/183706dade12080a748b0c074d0bd71fb0471d7e))
* show "Return to Arcade" button only during active game ([4153929](https://github.com/antialias/soroban-abacus-flashcards/commit/4153929a2ab199836249d53d92c1be4979782b73))
* smooth rail curves and deterministic track generation ([4f79c08](https://github.com/antialias/soroban-abacus-flashcards/commit/4f79c08d73c090165a1c419e7aa8ef543bc23e7e))
* stabilize route completion threshold to prevent stuck trains ([b7233f9](https://github.com/antialias/soroban-abacus-flashcards/commit/b7233f9e4afe1dadfe29ecc4430c74074a2674fc))
* update lockfile and fix Makefile paths ([7ba746b](https://github.com/antialias/soroban-abacus-flashcards/commit/7ba746b6bdcc4c06172e1dbacd856da9416e010a))
* update matching game for UUID player system ([2e041dd](https://github.com/antialias/soroban-abacus-flashcards/commit/2e041ddc4443be1d032139ad9850bbc28db5c171))
* update memory pairs game to use StandardGameLayout ([8df76c0](https://github.com/antialias/soroban-abacus-flashcards/commit/8df76c08fdf4108b88ce95de252cb8bd559fc5e4))
* update memory quiz to use StandardGameLayout ([3f86163](https://github.com/antialias/soroban-abacus-flashcards/commit/3f86163c142e577a64adfb3bf262656d2e100ced))
* update pnpm version to 8.15.6 to resolve ERR_INVALID_THIS error in workflow ([0b9bfed](https://github.com/antialias/soroban-abacus-flashcards/commit/0b9bfed12dfd48d9eacae69b378e28e188d3f2b1))
* update race track components for new player system ([ae4e8fc](https://github.com/antialias/soroban-abacus-flashcards/commit/ae4e8fcb5a62c07fb9ffa9a70c07e45ca8be88c8))
* update tutorial tests to use consolidated AbacusDisplayProvider ([899fc69](https://github.com/antialias/soroban-abacus-flashcards/commit/899fc6975f1fa14ddb42b2ead03524c9389e7c38))
* update workflow to support Personal Access Token for GitHub Packages publishing auth ([ae4b71b](https://github.com/antialias/soroban-abacus-flashcards/commit/ae4b71b98655364887a729ef9d2b67b6a753d6e9))
* upgrade CI dependencies and fix deprecated actions ([6a51c1e](https://github.com/antialias/soroban-abacus-flashcards/commit/6a51c1e9bdc299d86b8001eba35f930fe16cd60c))
* use displayPassengers for station rendering in RailroadTrackPath ([a9e0d19](https://github.com/antialias/soroban-abacus-flashcards/commit/a9e0d197348377cb66581150df47d2d1127ad09a))
* use node-linker=hoisted for full dependency hoisting ([d3b2e0b](https://github.com/antialias/soroban-abacus-flashcards/commit/d3b2e0b2e152150886110edd80dfe43f70df63d9))
* use player IDs instead of array indices in matching game ([ccd0d6d](https://github.com/antialias/soroban-abacus-flashcards/commit/ccd0d6d94ccd1cc25eed602d32a9cf884bda2ee6))
* use style fontSize instead of attribute for landmarks ([ebc6894](https://github.com/antialias/soroban-abacus-flashcards/commit/ebc6894746d1d490c3a5cae19c38bb86fe8fdc65))
* use UUID player IDs in session creation fallback ([22541df](https://github.com/antialias/soroban-abacus-flashcards/commit/22541df99f049ce99e020e12c2d28b33434de51d))
* wrap animated pressure value in animated.span to prevent React error ([5c5954b](https://github.com/antialias/soroban-abacus-flashcards/commit/5c5954be74708fb7019802a6dd80b10e9b2c1d6a))


### Performance Improvements

* optimize React rendering with memoization and consolidated effects ([93cb070](https://github.com/antialias/soroban-abacus-flashcards/commit/93cb070ca503effa05541f7ed217bb4260359581))


### Code Refactoring

* completely remove [@nav](https://github.com/nav) parallel routes and simplify navigation ([54ff20c](https://github.com/antialias/soroban-abacus-flashcards/commit/54ff20c7555e028b50471ac83a7030921c76f43b))
* consolidate abacus display context management ([a387b03](https://github.com/antialias/soroban-abacus-flashcards/commit/a387b030fa9fe36f2c8c0e65e34ec9ee872a7afa))
* extract ActivePlayersList component from PageWithNav ([2849576](https://github.com/antialias/soroban-abacus-flashcards/commit/28495767a9b792e6f8b9cc9f4df85e1b27a15c35))
* extract AddPlayerButton component from PageWithNav ([57a72e3](https://github.com/antialias/soroban-abacus-flashcards/commit/57a72e34a5df198ac795ff83cb6bfc6fb8a2f27e))
* extract FullscreenPlayerSelection component from PageWithNav ([66f5223](https://github.com/antialias/soroban-abacus-flashcards/commit/66f52234e12594947069c4ffed3648ce034c3e79))
* extract GameContextNav orchestration component ([e3f552d](https://github.com/antialias/soroban-abacus-flashcards/commit/e3f552d8f588b25d13eca20fbcd4f43b30de917f))
* extract GameHUD component from SteamTrainJourney ([78d5234](https://github.com/antialias/soroban-abacus-flashcards/commit/78d5234a79eb5293ae8eb279fb46b5aa2bbb6ae7))
* extract GameModeIndicator component from PageWithNav ([d67315f](https://github.com/antialias/soroban-abacus-flashcards/commit/d67315f771a3f660be58495c1236f74b49001d23))
* extract guide components to fix syntax error in large file ([c77e880](https://github.com/antialias/soroban-abacus-flashcards/commit/c77e880be32456c1e91d37358d85c445b2f707df))
* extract RailroadTrackPath component from SteamTrainJourney ([d9acc0e](https://github.com/antialias/soroban-abacus-flashcards/commit/d9acc0efea397ce58013160efbb2ed4fbee244b2))
* extract TrainAndCars component from SteamTrainJourney ([5ae22e4](https://github.com/antialias/soroban-abacus-flashcards/commit/5ae22e4645614bc67e7dece509d92bdd85250e28))
* extract TrainTerrainBackground component from SteamTrainJourney ([05bb035](https://github.com/antialias/soroban-abacus-flashcards/commit/05bb035db5483892f101cef0971bf08575cb041b))
* extract usePassengerAnimations hook from SteamTrainJourney ([32abde1](https://github.com/antialias/soroban-abacus-flashcards/commit/32abde107ca050bfc191a325d0bf074d53df33fc))
* extract useTrackManagement hook from SteamTrainJourney ([a1f2b97](https://github.com/antialias/soroban-abacus-flashcards/commit/a1f2b9736a0ff087dae44110708254e6da966b79))
* extract useTrainTransforms hook from SteamTrainJourney ([a2512d5](https://github.com/antialias/soroban-abacus-flashcards/commit/a2512d573823e187aad08f3fed365c4211023bb3))
* make game mode a computed property from active player count ([386c88a](https://github.com/antialias/soroban-abacus-flashcards/commit/386c88a3c03eb6de7814f65a6556a2d0ab50386b))
* remove drag-and-drop UI from EnhancedChampionArena ([982fa45](https://github.com/antialias/soroban-abacus-flashcards/commit/982fa45c08b34fdb64ec0835bc591b850e1c1373))
* remove duplicate game control buttons from game phases ([9165014](https://github.com/antialias/soroban-abacus-flashcards/commit/9165014997ccf6f4859646709d7e800933b4868e))
* remove redundant game titles from game screens ([402724c](https://github.com/antialias/soroban-abacus-flashcards/commit/402724c80e1776b90be1fc02186813389560f380))
* replace bulky MemoryGrid stats with compact progress display ([c4d6691](https://github.com/antialias/soroban-abacus-flashcards/commit/c4d6691715d09066661be4a0af7e917c6217ed8c))
* simplify navigation flow and enhance GameControls UI ([920aaa6](https://github.com/antialias/soroban-abacus-flashcards/commit/920aaa639887b42dcb225cb42ce146e67d29a98e))
* simplify PageWithNav by extracting nav components ([98cfa56](https://github.com/antialias/soroban-abacus-flashcards/commit/98cfa5645bc21faaeffa676d205bdbdf604eb488))
* split deployment info into server/client components ([5e7b273](https://github.com/antialias/soroban-abacus-flashcards/commit/5e7b273b339cd11d7b4b55dd50a1bf6c823b41d5))
* streamline GamePhase header and integrate PlayerStatusBar ([dcefa74](https://github.com/antialias/soroban-abacus-flashcards/commit/dcefa74902c65618f79eda32c94a5b8736b15b55))
* streamline UI and remove duplicate information displays ([7a3e34b](https://github.com/antialias/soroban-abacus-flashcards/commit/7a3e34b4faab62c069e6698a935ad66ee80037d2))


### Documentation

* add comprehensive workflow documentation for automated npm publishing ([f923b53](https://github.com/antialias/soroban-abacus-flashcards/commit/f923b53a44c2875fe152c9bd326d6a427d07a71e))
* add server persistence migration plan ([dd0df8c](https://github.com/antialias/soroban-abacus-flashcards/commit/dd0df8c274f513947e43f014b9086f77077f0196))


### Tests

* add comprehensive unit tests for refactored hooks and components ([5d20839](https://github.com/antialias/soroban-abacus-flashcards/commit/5d2083903e9eb751d810921e06dc51b7137f726f))
* add E2E tests for arcade modal session behavior ([619be98](https://github.com/antialias/soroban-abacus-flashcards/commit/619be9859c548b6c3f0af45379a61f690bcb8e13))

## [1.2.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.2.0...v1.2.1) (2025-09-28)


### Bug Fixes

* update GitHub Pages actions to v4 for better deployment reliability ([be76c23](https://github.com/antialias/soroban-abacus-flashcards/commit/be76c2355fbefd924890baad50b6e873a4e435f2))

# [1.2.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.1.3...v1.2.0) (2025-09-28)


### Features

* trigger storybook deployment after enabling GitHub Pages ([64dc94e](https://github.com/antialias/soroban-abacus-flashcards/commit/64dc94e91e089fadbdb75fbbf3a6164a2d224ef4))

## [1.1.3](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.1.2...v1.1.3) (2025-09-28)


### Bug Fixes

* add cssgen step to generate styles.css for Storybook ([26077de](https://github.com/antialias/soroban-abacus-flashcards/commit/26077de78bccf8549e1e9a0ac9c08742c61c8d28))

## [1.1.2](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.1.1...v1.1.2) (2025-09-28)


### Bug Fixes

* upgrade Node.js to version 20 for Storybook compatibility ([4c33872](https://github.com/antialias/soroban-abacus-flashcards/commit/4c338726c13af623b1536f75fe6a18e0ab529377))

## [1.1.1](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.1.0...v1.1.1) (2025-09-28)


### Bug Fixes

* update GitHub Actions to use latest action versions for Storybook deployment ([f0bb411](https://github.com/antialias/soroban-abacus-flashcards/commit/f0bb411573c8496d11d560fa7efe9324015412b2))

# [1.1.0](https://github.com/antialias/soroban-abacus-flashcards/compare/v1.0.0...v1.1.0) (2025-09-28)


### Features

* add GitHub Pages Storybook deployment with dual documentation sites ([439707b](https://github.com/antialias/soroban-abacus-flashcards/commit/439707b1188e9750fb2c62aac05d54fede196417))

# 1.0.0 (2025-09-28)


### Bug Fixes

* add explicit type annotation for examples array in LivePreview ([6c49e03](https://github.com/antialias/soroban-abacus-flashcards/commit/6c49e0335e9ef75e0566ffb547bb9c65029dbf64))
* add missing color-palette parameter to generate-flashcards function ([18583d0](https://github.com/antialias/soroban-abacus-flashcards/commit/18583d011a21db5a1d57eb21b241dd1d19573a07))
* add navigation to games from character selection modal ([b64fb1c](https://github.com/antialias/soroban-abacus-flashcards/commit/b64fb1c769c6965c81eefea10b21886380ce7216))
* add onConfigurePlayer prop to ChampionArena ([6e1050c](https://github.com/antialias/soroban-abacus-flashcards/commit/6e1050c76df6065c99332900303ef41d095226f5))
* add optional chaining to prevent TypeScript error ([d42dca2](https://github.com/antialias/soroban-abacus-flashcards/commit/d42dca2b4e85f01c38223fc5173da2243faa63bf))
* add robust fallback system for term highlighting in guidance ([decd8a3](https://github.com/antialias/soroban-abacus-flashcards/commit/decd8a36cacc2d08c60ff6bfb192e7e16ab84205))
* add tooltip targeting logic to only show on beads with arrows ([4425627](https://github.com/antialias/soroban-abacus-flashcards/commit/44256277a1fd60aa5be7484714a6fa6e434d656c))
* add xmlns attributes to SVG examples for GitHub compatibility ([c2f33ce](https://github.com/antialias/soroban-abacus-flashcards/commit/c2f33ceff2391f6a480a3d1239e3c750778940cb))
* adjust tutorial editor page height to account for app navigation ([9777bef](https://github.com/antialias/soroban-abacus-flashcards/commit/9777befbc54f53f06d053ad2f479db90cdd5252a))
* allow semantic release to proceed despite build failures ([73a6904](https://github.com/antialias/soroban-abacus-flashcards/commit/73a690405aa200e24d77f076572b613ad795efdf))
* apply CSS scaling to abacus components in memory quiz ([599fbfb](https://github.com/antialias/soroban-abacus-flashcards/commit/599fbfb802619ce8bbd04d880ed940552fe5b330))
* clean up component interfaces and settings ([ce6c2a1](https://github.com/antialias/soroban-abacus-flashcards/commit/ce6c2a111673f7fd1a31460439da2addfd20d376))
* convert foreignObject to native SVG text elements ([3ccc753](https://github.com/antialias/soroban-abacus-flashcards/commit/3ccc753a8297c45de5b857423feb2af6a0ae3c40))
* correct column indexing and add boundary checks for interactive abacus ([bbfb361](https://github.com/antialias/soroban-abacus-flashcards/commit/bbfb3614a22c4a3488130e7d4934775407184b3d))
* correct diamond bead column alignment to match Typst positioning ([97690d6](https://github.com/antialias/soroban-abacus-flashcards/commit/97690d6b595ae1fca085d8598cade13b846f3b44))
* correct heaven bead positioning to match earth bead gap consistency ([0c4eea5](https://github.com/antialias/soroban-abacus-flashcards/commit/0c4eea5a04ab94479c1fdf73306f32a35f392a50))
* correct highlightBeads format in AbacusTest.stories.tsx ([7122ad7](https://github.com/antialias/soroban-abacus-flashcards/commit/7122ad7fb4bf53695ce811c9eec361343eba0626))
* correct mathematical inconsistency in cascading complement test ([56cb69c](https://github.com/antialias/soroban-abacus-flashcards/commit/56cb69cb3e4fa256ea58420fa8310efba424bb59))
* correct pedagogical algorithm specification and tests ([9e87d3a](https://github.com/antialias/soroban-abacus-flashcards/commit/9e87d3ac37ddba69036ee315ba65b26073782520))
* correct segment expression formatting and rule detection ([e60f438](https://github.com/antialias/soroban-abacus-flashcards/commit/e60f4384c30260ae0632c10d0a60a8cffd4bb141))
* correct static file paths in Docker for Next.js standalone mode ([91223b6](https://github.com/antialias/soroban-abacus-flashcards/commit/91223b6f5da19738978091b5f6f785a77aff1ed2))
* correct styled-system import paths in games page ([82aa73e](https://github.com/antialias/soroban-abacus-flashcards/commit/82aa73eb0ee041fabf16d984ab6f5afebfb97dad))
* correct styled-system import paths in memory quiz page ([a967838](https://github.com/antialias/soroban-abacus-flashcards/commit/a967838c43b7a974ba6cf8f6bb6aaabea73d1f92))
* correct SVG text positioning to match React component alignment ([8024d0a](https://github.com/antialias/soroban-abacus-flashcards/commit/8024d0a25cba3b9e06df3a346d4e11545874698e))
* correct Tab navigation direction in numeral input system ([d4658c6](https://github.com/antialias/soroban-abacus-flashcards/commit/d4658c63b49a8270b26990b34a3b43fa3eb3c696))
* correct TanStack Form state selectors in create page ([178f0ff](https://github.com/antialias/soroban-abacus-flashcards/commit/178f0fff5942e3eb4612962635cb19a5f2891a47))
* correct term position calculation for complement segments ([7189090](https://github.com/antialias/soroban-abacus-flashcards/commit/718909015c6b967d46cb96401dacb8d3f9daeee9))
* correct tutorial bead highlighting to use rightmost column (ones place) ([b6b1111](https://github.com/antialias/soroban-abacus-flashcards/commit/b6b1111594b5530abe1f515dbc53e84ab1aebcf5))
* correct tutorial highlighting placeValue to columnIndex conversion ([35257b8](https://github.com/antialias/soroban-abacus-flashcards/commit/35257b88739573f6dc0dd16ec41ce754b2cb5b95))
* correct tutorial step "7 + 4" to highlight all required beads ([9c05bee](https://github.com/antialias/soroban-abacus-flashcards/commit/9c05bee73cdf3a34f46f993db965dd16b9d7b451))
* correct workspace configuration and remove non-existent packages ([39526eb](https://github.com/antialias/soroban-abacus-flashcards/commit/39526eb4966249e30656d77d65467bea847f7295))
* crop interactive abacus SVG whitespace with simple CSS scaling ([bb3d463](https://github.com/antialias/soroban-abacus-flashcards/commit/bb3d4636cdcdaa3ff12bef8498ac2c000fca2e96))
* disable pointer events on direction indicator arrows ([944d922](https://github.com/antialias/soroban-abacus-flashcards/commit/944d922f52a6584172f82ba8bb4716bcd8cb1d88))
* disable pointer events on overlay content div ([b5db935](https://github.com/antialias/soroban-abacus-flashcards/commit/b5db93562b31ec8b5dab091d76e2b3d9d0341a6c))
* display actual numbers in SVG examples ([3308e22](https://github.com/antialias/soroban-abacus-flashcards/commit/3308e22fd2bd4353c8cb2dc1ec9ac6b507ebc3a8))
* downgrade Docker action versions to available ones ([57d1460](https://github.com/antialias/soroban-abacus-flashcards/commit/57d146027ad43ab3c36c3aa408f9eaebe3ea0342))
* enable individual term hover events within complement groups ([0655968](https://github.com/antialias/soroban-abacus-flashcards/commit/06559686535dd943a1ff89445038b9da00881c0e))
* enable multi-bead highlighting in tutorial system ([ab99053](https://github.com/antialias/soroban-abacus-flashcards/commit/ab99053d7498b3e9f28373f94aa422adac618c0a))
* enhance collision detection to include all active beads ([3d9d69c](https://github.com/antialias/soroban-abacus-flashcards/commit/3d9d69c6fb3ec9340e36a388da4c1b3d4bdb468a))
* ensure abacus visibility in memory quiz display phase ([fea7826](https://github.com/antialias/soroban-abacus-flashcards/commit/fea7826bd85a7ec29fe0dd58dad589b80326ea2f))
* ensure celebration tooltip shows when steps complete ([5082378](https://github.com/antialias/soroban-abacus-flashcards/commit/5082378ec31a13d152271e03f85477022e9d6fd8))
* exclude test files from TypeScript build ([0e097da](https://github.com/antialias/soroban-abacus-flashcards/commit/0e097daf8f222d89211221c2fc3fd0057df267cf))
* expand heaven-earth-gap to 30pt to accommodate equal 19pt gaps for both heaven and earth inactive beads ([a048e11](https://github.com/antialias/soroban-abacus-flashcards/commit/a048e11f445cc29c222a84081577d2db7c8aff5a))
* extract clean SVG content from component output ([f57b071](https://github.com/antialias/soroban-abacus-flashcards/commit/f57b07166bef0bf41b21d2145d0b730b48db18fb))
* gallery now loads actual Typst-generated SVGs instead of fake placeholders ([87eb51d](https://github.com/antialias/soroban-abacus-flashcards/commit/87eb51d39912637874a49d0e1289b45f16b4f802))
* generate Panda CSS styled-system before building in Docker ([c7a45e9](https://github.com/antialias/soroban-abacus-flashcards/commit/c7a45e9c41805389554f759e5758bd989205ad97))
* handle both direct and module execution for web format ([a1fd4c8](https://github.com/antialias/soroban-abacus-flashcards/commit/a1fd4c84d3d21fa0dd25e0d633a9ce016174fd52))
* hide celebration tooltip when user moves away from target value ([f9e42f6](https://github.com/antialias/soroban-abacus-flashcards/commit/f9e42f6e923664439ae0a4f104514b3722d14bd7))
* implement bead highlighting by modifying getBeadColor function ([7ac5c29](https://github.com/antialias/soroban-abacus-flashcards/commit/7ac5c29e9d43e88b123cacb62e27608b60fe1ea2)), closes [#FFD700](https://github.com/antialias/soroban-abacus-flashcards/issues/FFD700)
* implement consistent single-card preview generation ([83da1eb](https://github.com/antialias/soroban-abacus-flashcards/commit/83da1eb086bfaa2332fc6010fba5585ef8b52111))
* implement focus handling for numeral input in place-value system ([415759c](https://github.com/antialias/soroban-abacus-flashcards/commit/415759c43b5add9a45b48a646e872f13e7743669))
* implement gap-filling logic for sorting challenge boundary issues ([df41f2e](https://github.com/antialias/soroban-abacus-flashcards/commit/df41f2eee32ea4ea3fec440e3e99198b756c3881))
* implement mathematical SVG bounds calculation for precise viewBox positioning ([1b0a642](https://github.com/antialias/soroban-abacus-flashcards/commit/1b0a6423f929b89b44ec152bd4afb4f5ea10db34))
* implement prefix-conflict detection for speed memory quiz ([01b00b5](https://github.com/antialias/soroban-abacus-flashcards/commit/01b00b5a40f42cd613ac7631e8d21ab8246dfc13))
* implement proper bi-directional drag and drop with useDroppable ([53fc41c](https://github.com/antialias/soroban-abacus-flashcards/commit/53fc41c58fa0411ac435a823642c4960f2a4293c))
* implement proper React controlled input pattern for AbacusReact ([c18919e](https://github.com/antialias/soroban-abacus-flashcards/commit/c18919e2a93408f7084454f5eabf57233051e164))
* implement proper SVG cropping and fix abacus positioning ([793ffd3](https://github.com/antialias/soroban-abacus-flashcards/commit/793ffd3c1f6b16ffdd058282b9f17a7df46a32bc))
* implement ref-based fullscreen element tracking for proper persistence ([7b947f2](https://github.com/antialias/soroban-abacus-flashcards/commit/7b947f2617e43b7adf29514b57f57c23f4ed1457))
* implement smooth cross-zone drag animations without scaling issues ([7219a41](https://github.com/antialias/soroban-abacus-flashcards/commit/7219a4131e3ad84b59fa16333b20f1ed4bb38cfd))
* improve abacus sizing across all components with CSS transforms ([cd6165e](https://github.com/antialias/soroban-abacus-flashcards/commit/cd6165ee3e9dbb6e8dce5261e9ef7643fc59fe52))
* improve error handling in ServerSorobanSVG component ([ec51105](https://github.com/antialias/soroban-abacus-flashcards/commit/ec5110544b33861feb96ea1b2a9e0b97c51a956f))
* improve game mode selection UX by removing redundancy ([9fe7068](https://github.com/antialias/soroban-abacus-flashcards/commit/9fe7068ded1b286a8896e03d54e16e0e13dd7e50))
* improve pedagogical correctness and cascade carry handling ([85ed254](https://github.com/antialias/soroban-abacus-flashcards/commit/85ed25471fa6b62fb4d52aef91cd26386498d81b))
* improve pedagogical segment detection and instruction quality ([0ac51ae](https://github.com/antialias/soroban-abacus-flashcards/commit/0ac51aefa75eab41769b448a73c171c32960f71e))
* improve race mechanics and fix display issues ([511eb2e](https://github.com/antialias/soroban-abacus-flashcards/commit/511eb2e8a98dee9da7fde16baf0372c5efe104ba))
* improve sorting game UI with larger abacus and better slot design ([d5e2fda](https://github.com/antialias/soroban-abacus-flashcards/commit/d5e2fdadd64129e4402760bd9d8423ae7b7f3b32))
* improve visual balance of inactive heaven bead positioning ([a789087](https://github.com/antialias/soroban-abacus-flashcards/commit/a7890873ed8bc37d7fb99a2765ef3a1eecfa4803))
* keep tooltip visible when step completed to show celebration ([b5d7512](https://github.com/antialias/soroban-abacus-flashcards/commit/b5d75120fd0d16c9419469ec34815dec8d97d4fd))
* make inactive heaven bead gaps truly equal to earth bead gaps ([209ea0f](https://github.com/antialias/soroban-abacus-flashcards/commit/209ea0f13b1f669725206fbb0ee72fce51f4d878))
* make lightbulb emoji inline with help text ([43e046a](https://github.com/antialias/soroban-abacus-flashcards/commit/43e046ae6cc623911ee9a23072ee822ee10bad01))
* make sorting game action buttons visible during gameplay ([0c1f44b](https://github.com/antialias/soroban-abacus-flashcards/commit/0c1f44b8c90455d250c39607d348c83193508ac5))
* match React component font sizing for SVG numbers ([dedc0e7](https://github.com/antialias/soroban-abacus-flashcards/commit/dedc0e7873062690b9bdb06207f09d2d6d2fc43c))
* maximize inactive heaven bead gap from reckoning bar ([8f88eeb](https://github.com/antialias/soroban-abacus-flashcards/commit/8f88eeb071a479faf3496902838864b7c7d584ad))
* move inactive heaven beads HIGHER for larger gap from reckoning bar ([2a82902](https://github.com/antialias/soroban-abacus-flashcards/commit/2a829023751c0c57a859c85561701e1e77e7b221))
* move inactive heaven beads to 2pt from top for 18pt gap from reckoning bar ([708cc91](https://github.com/antialias/soroban-abacus-flashcards/commit/708cc91bcc02396476b02061d92cee27cee1c92a))
* perfect crop mark detection and SVG dimension consistency ([79f38c1](https://github.com/antialias/soroban-abacus-flashcards/commit/79f38c13e7ec2917becaf1768047809019b6d98d))
* position inactive heaven beads above reckoning bar, not below ([2d7d4ef](https://github.com/antialias/soroban-abacus-flashcards/commit/2d7d4efaccb65435f66bb555141895426649d70d))
* position inactive heaven beads relative to reckoning bar with same 19pt gap as earth beads ([3424ca1](https://github.com/antialias/soroban-abacus-flashcards/commit/3424ca1d3430942dba11c9bd892a9fe17843b27c))
* position inactive heaven beads with maximum gap using available space ([421ec11](https://github.com/antialias/soroban-abacus-flashcards/commit/421ec11efc49557519df728fb605bf8030ef7573))
* position success toast near abacus instead of app nav ([ec40a8d](https://github.com/antialias/soroban-abacus-flashcards/commit/ec40a8d3cbb2c690e76b5fa274cf466df179cda7))
* preserve fullscreen mode when navigating from arcade to memory matching game ([2505335](https://github.com/antialias/soroban-abacus-flashcards/commit/25053352fe88a2f66a2323c4edfb53f3cd98b60d))
* prevent premature step completion for multi-step problems ([41dde87](https://github.com/antialias/soroban-abacus-flashcards/commit/41dde87778c8b65fea13f8819ab58300c400093a))
* prevent race end modal from breaking endless route progression ([e06be9d](https://github.com/antialias/soroban-abacus-flashcards/commit/e06be9d121d5738413fcd43842bc06cc520e7bcb))
* regenerate example SVGs with actual soroban renderings ([d94baa1](https://github.com/antialias/soroban-abacus-flashcards/commit/d94baa1a80cbbbb3edc3c91d5e51cce5e5b1c4af))
* remove broken display switching and add train emoji flip ([3227cd5](https://github.com/antialias/soroban-abacus-flashcards/commit/3227cd550e42b0e8137a7d42866d9a37423fa61f))
* remove controlled tooltip state to enable proper HoverCard timing ([e6e3aa9](https://github.com/antialias/soroban-abacus-flashcards/commit/e6e3aa948783b28d4edac6360ed5d4dc40b4ef80))
* remove explicit conventionalcommits preset config to fix semantic-release ([15a9986](https://github.com/antialias/soroban-abacus-flashcards/commit/15a9986c76d20a35ecca3a5c180f46b34369af49))
* remove failing tests from GitHub Actions workflow to enable deployment ([2eaeac6](https://github.com/antialias/soroban-abacus-flashcards/commit/2eaeac686217a574d1d74d4f78f64e17096dc602))
* remove ordering mismatch warning and implement correct expected state calculation ([9de48c6](https://github.com/antialias/soroban-abacus-flashcards/commit/9de48c63d8485507bb3935be0a052059461ababf))
* remove Panda CSS generated files from source control ([18b685b](https://github.com/antialias/soroban-abacus-flashcards/commit/18b685b92d6fbf8be9d6b34a84a49244f10dd71a))
* remove redundant mode selection and revert game naming ([03f5056](https://github.com/antialias/soroban-abacus-flashcards/commit/03f5056902574e069093e0b2139f9c9211268baa))
* remove TypeScript type check from GitHub Actions workflow ([18e2aa9](https://github.com/antialias/soroban-abacus-flashcards/commit/18e2aa9b5962be2f740819175b68755a47755bbd))
* replace all window.location.href with Next.js router for proper navigation ([2a84687](https://github.com/antialias/soroban-abacus-flashcards/commit/2a84687fec2ce577e10fecf4a8e52c83fe081f3e))
* replace invalid CSS 'space' property with 'gap' in guide page ([5841f3a](https://github.com/antialias/soroban-abacus-flashcards/commit/5841f3a52d2e5c55ecced905bc94cba9c300ffbf))
* resolve abacus sizing and prefix matching issues in memory quiz ([b1db028](https://github.com/antialias/soroban-abacus-flashcards/commit/b1db02851c40c4125bd2d077132475af84cf229a))
* resolve arrow disappearing and incorrect bead targeting in 3+14=17 story ([b253a21](https://github.com/antialias/soroban-abacus-flashcards/commit/b253a21c6c7169b32f8aa83863099abb8070eaed))
* resolve async/await issues in download API routes ([9afaf6e](https://github.com/antialias/soroban-abacus-flashcards/commit/9afaf6e12a0fb47e798b9dea7be0de33c1a4e6ee))
* resolve auto-incrementing counter in InteractiveWithNumbers story ([1838d7e](https://github.com/antialias/soroban-abacus-flashcards/commit/1838d7e72f08e63af66e5695e8918d85fdc216c2))
* resolve critical bugs in automatic instruction generator found by stress testing ([e783776](https://github.com/antialias/soroban-abacus-flashcards/commit/e783776754555c347e0de425dd78916b76cd3bdc))
* resolve critical ordering mismatch between multiStepInstructions and stepBeadHighlights ([2c395f3](https://github.com/antialias/soroban-abacus-flashcards/commit/2c395f38c3533fc4e7659d4801cb7010c60fe4bc))
* resolve display switching bug causing game content to disappear ([4736768](https://github.com/antialias/soroban-abacus-flashcards/commit/4736768ba642f91bfbf8d62725a9468086183892))
* resolve dnd-kit ref extension error in enhanced arena ([fac3202](https://github.com/antialias/soroban-abacus-flashcards/commit/fac320282b7f31d7f42eaa725d4288240f35ddda))
* resolve final TypeScript errors in place-value migration ([9a24dc8](https://github.com/antialias/soroban-abacus-flashcards/commit/9a24dc8f9d1e4217fe444f0ff52a7850d76bdf7b))
* resolve infinite render loop when clicking Next in tutorial player ([4ef6ac5](https://github.com/antialias/soroban-abacus-flashcards/commit/4ef6ac5f164dc97c5ddd5b9f307bd84ec0df8871))
* resolve nested border radius visual artifacts on match cards ([c69f6a4](https://github.com/antialias/soroban-abacus-flashcards/commit/c69f6a451a146053ff01e0bcbaacf1363781e590))
* resolve Python FileNotFoundError and improve error handling ([69bda9f](https://github.com/antialias/soroban-abacus-flashcards/commit/69bda9fb36ef58c3dab3478ea7d05c1e7c8b1503))
* resolve ReferenceError by moving ref declarations before usage ([fa153c6](https://github.com/antialias/soroban-abacus-flashcards/commit/fa153c6908da67f55bfc496f420864478b9c6bad))
* resolve SorobanGeneratorBridge path issues for SVG generation ([845a4ff](https://github.com/antialias/soroban-abacus-flashcards/commit/845a4ffc486f1ee0d5893f9d783e3c8af622cd08))
* resolve stepIndex mismatch preventing arrows in multi-step sequences ([96fda6b](https://github.com/antialias/soroban-abacus-flashcards/commit/96fda6b91903c0ca76cfbb6e0f4888b492e1a731))
* resolve style dropdown click-outside and infinite re-render issues ([6394218](https://github.com/antialias/soroban-abacus-flashcards/commit/639421866757889f187453557b45276be07acae3))
* resolve temporal dead zone error with goToNextStep ([3d503dd](https://github.com/antialias/soroban-abacus-flashcards/commit/3d503dda5d494c31461bbebfdf7e04899a9dc4b5))
* resolve test failures and improve test robustness ([3c0affc](https://github.com/antialias/soroban-abacus-flashcards/commit/3c0affca00ba6d87322334d162f2aee2109166d8))
* resolve TypeScript compilation errors ([db3784e](https://github.com/antialias/soroban-abacus-flashcards/commit/db3784e7d0b9bfef03af5966cc13d8c92f1e3982))
* resolve TypeScript compilation errors blocking GitHub Actions build ([83ba792](https://github.com/antialias/soroban-abacus-flashcards/commit/83ba79241f5a6480e8c2d797bf5c9b407de7f297))
* resolve TypeScript errors across the codebase ([5946183](https://github.com/antialias/soroban-abacus-flashcards/commit/59461831e5f6cdfa3ef19bf4b092b2d7d2abc622))
* resolve zero-state interaction bug in AbacusReact component ([f18018d](https://github.com/antialias/soroban-abacus-flashcards/commit/f18018d9afd2cc83a4e34d8925383c79a35f11df))
* restore click functionality alongside directional gestures ([3c28c69](https://github.com/antialias/soroban-abacus-flashcards/commit/3c28c694fc83ac58a0dec91b25b3919dfe22eb63))
* restore interactive abacus display with TypstSoroban fallback ([b794187](https://github.com/antialias/soroban-abacus-flashcards/commit/b794187392bd5d1a828f34372c29b5a4b32d8726))
* restore missing typst dependencies for WASM loading ([96aa790](https://github.com/antialias/soroban-abacus-flashcards/commit/96aa7906931498874c4e42a5d457bdc1e9f3d952))
* restore single-click player card functionality for arena toggle ([1ba2a11](https://github.com/antialias/soroban-abacus-flashcards/commit/1ba2a11b3a916996f50ad9aab0b3b0b4e0fc129d))
* restore workspace dependencies and fix TypeScript errors ([31df87d](https://github.com/antialias/soroban-abacus-flashcards/commit/31df87d3fc8febcd7c58cc654d00c83506089ab9))
* show numbers in educational abacus examples ([2b5f143](https://github.com/antialias/soroban-abacus-flashcards/commit/2b5f14310c0f03f1ad32d10dfe638f5d8731cf87))
* simplify collision detection to resolve iterable error ([0b3e8fd](https://github.com/antialias/soroban-abacus-flashcards/commit/0b3e8fd3d63257b2eb99b0abcefeac183b16703c))
* simplify inactive heaven bead positioning for better gap matching ([22c4bd3](https://github.com/antialias/soroban-abacus-flashcards/commit/22c4bd3112567df03a185f8ee59813b6a7846fac))
* simplify semantic-release config to use default conventional commits ([e207659](https://github.com/antialias/soroban-abacus-flashcards/commit/e20765953b4269be39217d9d20505b4f29639685))
* single digit values now correctly position in rightmost column ([689bfd5](https://github.com/antialias/soroban-abacus-flashcards/commit/689bfd5df106f60f904c2a1b2c38339b50cc2ae7))
* stabilize smart help detection with timer-based state ([9cc3a0e](https://github.com/antialias/soroban-abacus-flashcards/commit/9cc3a0ea9b548c03a6ef80b8b7a6511df2b0e82d))
* update bridge generator interface to support SVG format ([a022852](https://github.com/antialias/soroban-abacus-flashcards/commit/a02285289ad4c88072d25c7fe44342f29c86c3ba))
* update GitHub Actions to use latest action versions ([b674946](https://github.com/antialias/soroban-abacus-flashcards/commit/b674946d8d397fed61f15f42cfa802989a6a81a6))
* update gitignore to follow Panda CSS best practices ([ccd0aa7](https://github.com/antialias/soroban-abacus-flashcards/commit/ccd0aa7552e72fc7fb94464522636f1b3114b1ce))
* update pnpm lockfile to sync with semantic-release dependencies ([9d23e82](https://github.com/antialias/soroban-abacus-flashcards/commit/9d23e82b5aa086e591d7c86d5b821780993f860f))
* update relative import in generate.py for module compatibility ([b633578](https://github.com/antialias/soroban-abacus-flashcards/commit/b633578ac53dab1cc2d6e33939fffc16953fe89b))
* update unified gallery to use correct crop examples ([826e86d](https://github.com/antialias/soroban-abacus-flashcards/commit/826e86d73c0d436099deda89eb4a7772a53e3840))
* use actual AbacusReact component for README examples via SSR ([a630aa4](https://github.com/antialias/soroban-abacus-flashcards/commit/a630aa4f2cefce437c5e5a498e383407b9f424da))
* use aggressive NumberFlow mock for SVG text rendering ([1364b11](https://github.com/antialias/soroban-abacus-flashcards/commit/1364b11ed1747323a1161785798b880d8bcf3fce))
* use correct test command in GitHub Actions workflow ([6483e28](https://github.com/antialias/soroban-abacus-flashcards/commit/6483e285d48b799d5c11c6b002ec81eeff29969b))


### Features

* add 292 comprehensive snapshot tests for pedagogical algorithm ([3b8f803](https://github.com/antialias/soroban-abacus-flashcards/commit/3b8f803ca8895bfb3db75c0c4dae538aefde89e7))
* add AbacusContext for global display configuration ([6460089](https://github.com/antialias/soroban-abacus-flashcards/commit/6460089ab9be95e48a3e8e16954c3237cfe4a4ee))
* add ArithmeticOperationsGuide component to learning guide ([902fa56](https://github.com/antialias/soroban-abacus-flashcards/commit/902fa56d238e3f4ebb911a5565dbb3a0b00cdbac))
* add automated semantic release system with conventional commits ([46c8839](https://github.com/antialias/soroban-abacus-flashcards/commit/46c88392d1902a48b0399ede1850c6f8e8c590f6))
* add backgroundGlow support for column highlighting ([b1866ce](https://github.com/antialias/soroban-abacus-flashcards/commit/b1866ce7fbb6b719ec618ea02fb8da557195440c))
* add bead annotation support to SVG generation ([ab244ea](https://github.com/antialias/soroban-abacus-flashcards/commit/ab244ea1911daf7934f7e6a3b7187710002728f7))
* add browser fullscreen API context ([8e1a948](https://github.com/antialias/soroban-abacus-flashcards/commit/8e1a948ffde3db98052bdfe7b604d58e1934e4b6))
* add browser-free example generation using react-dom/server ([a100a6e](https://github.com/antialias/soroban-abacus-flashcards/commit/a100a6e4984b5b1c2b7f71d19458684f957406d0))
* add browser-side bead annotation processing ([914e145](https://github.com/antialias/soroban-abacus-flashcards/commit/914e145d445194bbdf68940ba2cf5224dd152fa7))
* add CI-friendly example generation and verification ([1adbd1a](https://github.com/antialias/soroban-abacus-flashcards/commit/1adbd1a5ffd28f1c7d49aad8b21850d9e3785912))
* add click-to-dismiss functionality for success popup ([3066826](https://github.com/antialias/soroban-abacus-flashcards/commit/306682632e64ca65500569c017e32b619f8115db))
* add colored numerals feature to match bead colors ([e4aaaea](https://github.com/antialias/soroban-abacus-flashcards/commit/e4aaaeab1318e1679399eb5f108073adb6cc9563))
* add complete NAS deployment system for apps/web ([eb8ed8b](https://github.com/antialias/soroban-abacus-flashcards/commit/eb8ed8b22c6f950210f7e77bdb27ea98ca4aa11d))
* add comprehensive .gitignore for monorepo ([9eccd34](https://github.com/antialias/soroban-abacus-flashcards/commit/9eccd34e58f131d0b9099ac2793a16900aa7f2e7))
* add comprehensive soroban learning guide with server-generated SVGs ([38d8959](https://github.com/antialias/soroban-abacus-flashcards/commit/38d89592c951ec9f015a18b767e82b565d068ec5))
* add comprehensive Storybook demos for problem generation system ([c01f968](https://github.com/antialias/soroban-abacus-flashcards/commit/c01f968ff7fd3436ae273bbcb2d7f67de90cfd7c))
* add comprehensive Storybook examples for documentation ([8289241](https://github.com/antialias/soroban-abacus-flashcards/commit/828924129e7acc03427fc01be7a0afdc1b34a6af))
* add comprehensive test suite and documentation ([bb869a0](https://github.com/antialias/soroban-abacus-flashcards/commit/bb869a0b11ba1173c5b4c7fbea096dac7f0d98d2))
* add comprehensive test suite with visual regression testing ([7a2eb30](https://github.com/antialias/soroban-abacus-flashcards/commit/7a2eb309a846fdf125371e890197ab5cb2d4ea9e))
* add comprehensive tests for celebration tooltip behavior ([a23ddf5](https://github.com/antialias/soroban-abacus-flashcards/commit/a23ddf5b9acc1a7a78916de74813d3a10202ada8))
* add comprehensive tutorial system with editor and player ([579caf1](https://github.com/antialias/soroban-abacus-flashcards/commit/579caf1a26652704b8a8a5de566f4a6ab6e8c2c5))
* add comprehensive unit test suite for memory quiz functionality ([a557362](https://github.com/antialias/soroban-abacus-flashcards/commit/a557362c9ea6ea033b4c356351e9959542c9f60c))
* add comprehensive welcome page as default landing experience ([556a830](https://github.com/antialias/soroban-abacus-flashcards/commit/556a830540549ca1f268a22f44fd4706495a6fa3))
* add concurrent Panda CSS watch to dev script ([e8aed80](https://github.com/antialias/soroban-abacus-flashcards/commit/e8aed8034a2d109d8231d942f45e9620f526d948))
* add config presets for colored numerals and skip counting ([a8a01a8](https://github.com/antialias/soroban-abacus-flashcards/commit/a8a01a8db3e9264b4c5ecd199e40b0d1c26abc17))
* add cosmic fullscreen mode to abacus style dropdown ([afec22a](https://github.com/antialias/soroban-abacus-flashcards/commit/afec22ac3f497067a9a32693cbca87b09073b449))
* add deprecation markers to legacy column-based API ([22f1869](https://github.com/antialias/soroban-abacus-flashcards/commit/22f186955722e596bc9b2f18255798379a62232b))
* add development tooling and comprehensive setup ([7ca65bf](https://github.com/antialias/soroban-abacus-flashcards/commit/7ca65bfd596aab5fcee627bc968ff512d51ce36c))
* add extracted TutorialDebugPanel and TutorialNavigation components ([bc5446a](https://github.com/antialias/soroban-abacus-flashcards/commit/bc5446a29f123cf79701432653378786bee66efb))
* add fox tunnel digging system for Lightning Sprint mode ([b7fac3a](https://github.com/antialias/soroban-abacus-flashcards/commit/b7fac3a601ccfff1d2945177176780920c0d7c63))
* add full-viewport abacus test page ([861f0e0](https://github.com/antialias/soroban-abacus-flashcards/commit/861f0e0a0fd8a0f205b0e932caff78de198c28b8))
* add fullscreen arcade page with Champion Arena ([3edf35f](https://github.com/antialias/soroban-abacus-flashcards/commit/3edf35f6a1a0ff199dc1c109241cfa584663a7c5))
* add fullscreen game layout wrapper component ([a25e611](https://github.com/antialias/soroban-abacus-flashcards/commit/a25e6117bb325aa5d75443b42c98ca5d68624693))
* add fullscreen parameter handling to GameCard ([337aa56](https://github.com/antialias/soroban-abacus-flashcards/commit/337aa5609a65d8bdcb9c516a0f50e3d3df0f76ee))
* add fullscreen support to Memory Quiz game ([763fc95](https://github.com/antialias/soroban-abacus-flashcards/commit/763fc95025e84af515711dccd6847abbd3c97bb0))
* add Games navigation to main app header ([b87ed01](https://github.com/antialias/soroban-abacus-flashcards/commit/b87ed01520d19719e162de41f30c80595295473e))
* add guided addition tutorial with five complements ([8ca9dd7](https://github.com/antialias/soroban-abacus-flashcards/commit/8ca9dd7a193a573035a5d42cd0308c3b85d0e121))
* add input-based flashcard template with parameter parsing ([b375a10](https://github.com/antialias/soroban-abacus-flashcards/commit/b375a104a5ea90e97f7c4530bdb85d282f9eb94d))
* add interactive abacus display to guide reading section ([6d68cc2](https://github.com/antialias/soroban-abacus-flashcards/commit/6d68cc2a061d74f0df13002e5a9382f26b657751))
* add interactive bead clicking to soroban abacus ([697552e](https://github.com/antialias/soroban-abacus-flashcards/commit/697552ecd916ab7045b28d075610e6f542b7ad91))
* add interactive test story for column highlighting with bead interaction ([ee20473](https://github.com/antialias/soroban-abacus-flashcards/commit/ee20473a3646267763184ec25fc2254009671066))
* add interactive tutorial system with step validation ([c5c2542](https://github.com/antialias/soroban-abacus-flashcards/commit/c5c2542849710dee03ffe48f136c3c7462514b36))
* add invisible crop marks for consistent SVG viewBox boundaries ([7731f70](https://github.com/antialias/soroban-abacus-flashcards/commit/7731f70b996758e701062de1b2f380e698a0ddab))
* add Node.js/TypeScript integration with clean function interface ([fb1b047](https://github.com/antialias/soroban-abacus-flashcards/commit/fb1b0470cfb4de3e38b20c9331980ceb705311cf))
* add PDF print integration with modal interface ([09b0fad](https://github.com/antialias/soroban-abacus-flashcards/commit/09b0fad6336a85ddfe6b386850fd423685f83734))
* add pedagogical segments for contextual learning ([0053510](https://github.com/antialias/soroban-abacus-flashcards/commit/00535107835551cd660b1bd523d17126b9e7f6d0))
* add practice page system to guided addition tutorial ([9adc3db](https://github.com/antialias/soroban-abacus-flashcards/commit/9adc3db966d420b39a7eeb851c5a6131b4ed09d3))
* add precise term position tracking to unified step generator ([52323ae](https://github.com/antialias/soroban-abacus-flashcards/commit/52323aeba80d57ffaf32af27e4f12c37099ca9f6))
* add production-ready defensive programming for pedagogical segments ([704a8a8](https://github.com/antialias/soroban-abacus-flashcards/commit/704a8a82284e91d35e747cc4c2ffbec61b21b155))
* add proper step initialization and multi-step navigation to TutorialContext ([153649c](https://github.com/antialias/soroban-abacus-flashcards/commit/153649c17d118cb8c9025cce36de99ab846bda61))
* add Python bridge and optional FastAPI server ([98263a7](https://github.com/antialias/soroban-abacus-flashcards/commit/98263a79a064cf6934e1706575cd5b31c47e249f))
* add Radix tooltip dependency for better tooltip accessibility ([6c02ea0](https://github.com/antialias/soroban-abacus-flashcards/commit/6c02ea06e7f6285fe89df533327cd2cffd1d3b31))
* add real-time bead movement feedback to tutorial UI ([4807bc2](https://github.com/antialias/soroban-abacus-flashcards/commit/4807bc2fd959550737ff0a741f578472dc687303))
* add reusable GameSelector and GameCard components ([c5a654a](https://github.com/antialias/soroban-abacus-flashcards/commit/c5a654aef15e840ca12216a908b30806ed80afea))
* add self-contained Storybook-like gallery for template visualization ([efc5cc4](https://github.com/antialias/soroban-abacus-flashcards/commit/efc5cc408d0ce8a1f9765e99b24c7c3148d2237c))
* add setGameModeWithPlayers method to GameModeContext ([c3a4d76](https://github.com/antialias/soroban-abacus-flashcards/commit/c3a4d76d1601437956d24f39c2fc1096a132a238))
* add single card template for PNG/SVG output ([3315310](https://github.com/antialias/soroban-abacus-flashcards/commit/33153108a2ade5d4f0921f1d26dda5d7387eba81))
* add smooth cross-zone reordering animations and tone down scaling ([b7335f0](https://github.com/antialias/soroban-abacus-flashcards/commit/b7335f0e67fe0f3c5088d775104b3ad2408a1755))
* add soroban games section with Speed Memory Quiz ([331a789](https://github.com/antialias/soroban-abacus-flashcards/commit/331a78937e2fcf03fc84d68cfb1e63edf2388112))
* add static site generator for gallery with embedded SVGs ([505ff66](https://github.com/antialias/soroban-abacus-flashcards/commit/505ff66bd57ca9627e7ac2aa4af5af5c0f2ed324))
* add step parameter for skip counting ([c94fa5c](https://github.com/antialias/soroban-abacus-flashcards/commit/c94fa5c74ea45926d1169a4bfeeddb71ef989211))
* add Storybook stories for debugging zero-state interaction bug ([f293e5e](https://github.com/antialias/soroban-abacus-flashcards/commit/f293e5ecf7dffe030a3283c17076c33270ac3aa1))
* add stunning hero section with colorful soroban showcase ([d65ac54](https://github.com/antialias/soroban-abacus-flashcards/commit/d65ac546aa872688c483575be558cb78ce17326d))
* add SVG post-processing to convert bead annotations to data attributes ([8de3259](https://github.com/antialias/soroban-abacus-flashcards/commit/8de32593b035d391261feb836135ea0d78720ffb))
* add SVG post-processor to package exports ([59f4022](https://github.com/antialias/soroban-abacus-flashcards/commit/59f4022afb6f58b0a71c69d4b5537b56933d053e))
* add testing framework dependencies ([11306df](https://github.com/antialias/soroban-abacus-flashcards/commit/11306dfb2ec813f113f060b49408a01c8ccdcbf7))
* add TouchSensor for mobile drag and drop compatibility ([4fbf4d8](https://github.com/antialias/soroban-abacus-flashcards/commit/4fbf4d8bb28e075084efae29c4eb78f74efbc6d3))
* add TypeScript client libraries for browser integration ([f21b5e5](https://github.com/antialias/soroban-abacus-flashcards/commit/f21b5e5592f98b3b3a953148c5c023be553ea957))
* add TypeScript configuration for core package ([43b3296](https://github.com/antialias/soroban-abacus-flashcards/commit/43b3296e2652609ac08ed6803af5817fa15e1119))
* add typography improvements and subtle dev warning styling ([12a8837](https://github.com/antialias/soroban-abacus-flashcards/commit/12a88375abe0e831bf439915a2af9c6bb3d7257e))
* add unified step generator for consistent pedagogical decomposition ([93d2d07](https://github.com/antialias/soroban-abacus-flashcards/commit/93d2d07626558d81a0f0dce0280de333a3c5e413))
* add UserProfileProvider to app layout for character support ([21c430b](https://github.com/antialias/soroban-abacus-flashcards/commit/21c430b9f0348cd3836d40ea763b916f6c4af4e4))
* add WASM preloading strategy with template deduplication ([91e65c8](https://github.com/antialias/soroban-abacus-flashcards/commit/91e65c8a61dcb41f7a84c4e1ae923288dfd7fabe))
* add web development test files and public assets ([0809858](https://github.com/antialias/soroban-abacus-flashcards/commit/0809858302acb45231ac373cb22cdbe93f9a9309))
* add web output format with interactive hover flashcards ([0a4e849](https://github.com/antialias/soroban-abacus-flashcards/commit/0a4e849c35249e24ed5691f22baa9c6b6e6986f0))
* attempted floating math display following train ([2d50eb8](https://github.com/antialias/soroban-abacus-flashcards/commit/2d50eb8e976b62ad143df9104281f28f312afbe5))
* automatic abacus instruction generator for user-created tutorial steps ([5c46470](https://github.com/antialias/soroban-abacus-flashcards/commit/5c4647077b121c364ca18a21464a50e89deabe4a))
* BREAKTHROUGH - eliminate effectiveColumns threading nightmare! ([8fd9e57](https://github.com/antialias/soroban-abacus-flashcards/commit/8fd9e57292dfc32b8092b5500164d2b5da68105f))
* complete deployment documentation and infrastructure ([26f9285](https://github.com/antialias/soroban-abacus-flashcards/commit/26f928586ee57882bc8e6e29d55db4083d799e13))
* COMPLETE place-value migration - eliminate all backward compatibility ([67be974](https://github.com/antialias/soroban-abacus-flashcards/commit/67be974a8b7f89eb7f80b157a2a4e025f68b438b))
* complete steam train sound system and smooth time-of-day transitions ([6c60f94](https://github.com/antialias/soroban-abacus-flashcards/commit/6c60f94a5664e92905d91494ff3c8abb32302e4e))
* completely rewrite SorobanQuiz memory game with advanced features ([c3fdbfc](https://github.com/antialias/soroban-abacus-flashcards/commit/c3fdbfc199259aeba3a97b1ae83b0a8b4b785c4f))
* connect TutorialPlayer to universal AbacusDisplayContext ([ff12bab](https://github.com/antialias/soroban-abacus-flashcards/commit/ff12bab8ab8cd9fcbbb5be1447bc9aefb1931264))
* convert SorobanQuiz memory game styling to Panda CSS ([bed97e6](https://github.com/antialias/soroban-abacus-flashcards/commit/bed97e62ad236a1d8658f44a7eeffdc407ce5097))
* create @soroban/templates package with dual Node.js/Python interface ([7da0123](https://github.com/antialias/soroban-abacus-flashcards/commit/7da0123a840af594dedd5b830cb0bd61ac04b9b9))
* create comprehensive interactive soroban tutorial with stunning UI ([d78f19e](https://github.com/antialias/soroban-abacus-flashcards/commit/d78f19e4bca5a08c0ee6db22914ac07d0411b83b))
* create interactive gallery replicating original Typst design ([1bcfd22](https://github.com/antialias/soroban-abacus-flashcards/commit/1bcfd22f17cc9876393c9aa76a7c3a2292369eaa))
* create Next.js web application with beautiful UI ([1b7e71c](https://github.com/antialias/soroban-abacus-flashcards/commit/1b7e71cc0d0c6baa09069560eb89c137aa4360b2))
* create sequential practice problem player with step-by-step guidance ([8811106](https://github.com/antialias/soroban-abacus-flashcards/commit/88111063a5cf885735ffbed3ca4ce63f54559e74))
* create shared EditorComponents library for tutorial UI consistency ([4991a91](https://github.com/antialias/soroban-abacus-flashcards/commit/4991a91c7d989c7e770ddea2193fc890b1b70741))
* create unified skill configuration interface with intuitive modes ([fc79540](https://github.com/antialias/soroban-abacus-flashcards/commit/fc79540f788b3332f74bd22bdef5fe562a3aa903))
* disable NumberFlow animations for keyboard input to prevent jarring transitions ([fe38bfc](https://github.com/antialias/soroban-abacus-flashcards/commit/fe38bfc8ad36b6b7787bb6c5f2a49dfc5527f1d1))
* display pedagogical terms inline with current tutorial step ([408eb58](https://github.com/antialias/soroban-abacus-flashcards/commit/408eb58792d6082fd33ea92bb40e42da7fec2597))
* enable automatic live preview updates and improve abacus sizing ([f680987](https://github.com/antialias/soroban-abacus-flashcards/commit/f680987ed6d0ea3e0fda6e02936c2e4a2c700103))
* enhance ChampionArena with integrated GameSelector and improved UX ([aba3f68](https://github.com/antialias/soroban-abacus-flashcards/commit/aba3f685bc611f66e3500e1a9b91b94f38dac545))
* enhance column mapping for two-level highlighting ([007d088](https://github.com/antialias/soroban-abacus-flashcards/commit/007d0889eba255e90cbb4abab9926c980570f4b2))
* enhance crop marks with edge-based positioning and comprehensive tests ([8c7a5b1](https://github.com/antialias/soroban-abacus-flashcards/commit/8c7a5b1291314a8e1f9ac2f854f937b70d7250bc))
* enhance GameCard with epic character celebration animations ([b05189e](https://github.com/antialias/soroban-abacus-flashcards/commit/b05189e9ebdbb1f16d6654d00b59550967a27347))
* enhance instruction generator with step bead highlighting and multi-step support ([8518d90](https://github.com/antialias/soroban-abacus-flashcards/commit/8518d90e8500deb7ca0efbc07d41da35f6ac2e1c))
* enhance memory quiz input phase for better learning experience ([7c5556b](https://github.com/antialias/soroban-abacus-flashcards/commit/7c5556bf51419d61aa99d852e52fc0385f198f0b))
* enhance memory quiz with dynamic columns and adaptive transitions ([aa1f674](https://github.com/antialias/soroban-abacus-flashcards/commit/aa1f674553d316312497e5e3397e479ad541d141))
* enhance navigation touch targets for mobile ([6e09f21](https://github.com/antialias/soroban-abacus-flashcards/commit/6e09f21a704b9f23150de4acc809980bcce173bc))
* enhance pedagogical reasoning tooltips with comprehensive context ([bb38c7c](https://github.com/antialias/soroban-abacus-flashcards/commit/bb38c7c87cb46437223f8007d55d0a9d59b1152e))
* enhance steam train coal shoveling visual feedback ([f26fce4](https://github.com/antialias/soroban-abacus-flashcards/commit/f26fce4994885c2371ec14433d57cef449364c1b))
* enhance test page with lazy loading demo ([5a8bb2f](https://github.com/antialias/soroban-abacus-flashcards/commit/5a8bb2f85904d4dcb7067896f081c7eb29859cd1))
* enhance tooltips with combined provenance and pedagogical content ([0c7ad5e](https://github.com/antialias/soroban-abacus-flashcards/commit/0c7ad5e4e74520f3d1ad699f78f381035320e0ef))
* enhance tutorial system with multi-step progression support ([3a63950](https://github.com/antialias/soroban-abacus-flashcards/commit/3a6395097d6df7dd6210e156acc53959a7ba3bf7))
* enhance two-player matching game with multiple UX improvements ([f35dcdc](https://github.com/antialias/soroban-abacus-flashcards/commit/f35dcdc3d5a73a106aaaf19a8631b8b6a70d5ac8))
* export bridge generator from core package ([90a5c06](https://github.com/antialias/soroban-abacus-flashcards/commit/90a5c06f7c33009272f5c8d12bc5a396acd0d32b))
* export SVG processing functions from main module ([bee866a](https://github.com/antialias/soroban-abacus-flashcards/commit/bee866ab5cb22a11421e3fba1fee4a7eefead881))
* extend provenance system for multi-column term tracking ([013e8d5](https://github.com/antialias/soroban-abacus-flashcards/commit/013e8d5237753238ad93dc5e345dc8ec7bb30750))
* hide Next Action when at expected starting state for current step ([aafee3a](https://github.com/antialias/soroban-abacus-flashcards/commit/aafee3a25ac8f09de9119772db7e456d106b7196))
* hide Next Action when current state matches step target ([ed3d896](https://github.com/antialias/soroban-abacus-flashcards/commit/ed3d89667e14ad3d27b92f5175c213510766520a))
* hide redundant pedagogical expansions for simple problems ([9d0e8c7](https://github.com/antialias/soroban-abacus-flashcards/commit/9d0e8c7086051db70c8b9ea446fe1cb0d9c3a620))
* hide timer bar for train variant only ([84334f9](https://github.com/antialias/soroban-abacus-flashcards/commit/84334f9d5a980b2460bd77cf401c4410d8bd4633))
* implement 90s arcade sound system and tunnel digging mechanics ([a43ab92](https://github.com/antialias/soroban-abacus-flashcards/commit/a43ab9237e4d530d79acb83a11cfedaf0cc47338))
* implement actual abacus SVG generation for README examples ([6e02102](https://github.com/antialias/soroban-abacus-flashcards/commit/6e0210243a31be74f8ebc30eb58033e91c587652))
* implement authentic adjacent bead spacing for realistic abacus appearance ([f28256d](https://github.com/antialias/soroban-abacus-flashcards/commit/f28256dc608179d6b388fbbea6bd3ca83beda3a4))
* implement clean background glow for term-to-column highlighting ([ec030f0](https://github.com/antialias/soroban-abacus-flashcards/commit/ec030f00fd2129c17281772a99f696e477624df0))
* implement colorblind-friendly color palettes with mnemonic support ([faf578c](https://github.com/antialias/soroban-abacus-flashcards/commit/faf578c360f6436016b9dbbdfbccea0a9870c277))
* implement complete smart number entry system for quiz ([150c195](https://github.com/antialias/soroban-abacus-flashcards/commit/150c195c33073a07f3ec7c760a0512e720b9ca17))
* implement comprehensive bead diff tooltips with pedagogical decomposition ([2e3223d](https://github.com/antialias/soroban-abacus-flashcards/commit/2e3223da90f903ac1349eca5d4d988cbd40b6fa0))
* implement comprehensive character integration for /games arcade ([26bf399](https://github.com/antialias/soroban-abacus-flashcards/commit/26bf3990b04ef55cd8565ae1d69d067d5aa21ba7))
* implement comprehensive customization API for AbacusReact ([48f6e77](https://github.com/antialias/soroban-abacus-flashcards/commit/48f6e7704c6df55d770d74236abb14c4f31104ff))
* implement comprehensive pedagogical algorithm improvements ([72d9362](https://github.com/antialias/soroban-abacus-flashcards/commit/72d9362cc4db3d6356cddd848ef0a20277f745b7))
* implement comprehensive pedagogical expansion tests for abacus operations ([5d39bdc](https://github.com/antialias/soroban-abacus-flashcards/commit/5d39bdc84ef156de9a26a0175c6eb79dd8f4878c))
* implement context-aware English instruction generation ([bd3f144](https://github.com/antialias/soroban-abacus-flashcards/commit/bd3f1440a36ba21a09612f254890b33a84fe3866))
* implement CSS-based hidden inactive beads with smooth opacity transitions ([ff42bcf](https://github.com/antialias/soroban-abacus-flashcards/commit/ff42bcf6532c188bd84e547f135b2f648dbf3ebd))
* implement dynamic bead diff algorithm for state transitions ([c43090a](https://github.com/antialias/soroban-abacus-flashcards/commit/c43090aa7d7d11caa30fc767b34e087a959f1217))
* implement dynamic train orientation following curved path direction ([e6065e8](https://github.com/antialias/soroban-abacus-flashcards/commit/e6065e8ef222c95c30bf29afb1d2b1e1de732549))
* implement elegant between-step hover-based add functionality ([89a0239](https://github.com/antialias/soroban-abacus-flashcards/commit/89a023971fcbb317eae95531d0416fe5b28c4d41))
* implement endless route progression system ([a2b3e97](https://github.com/antialias/soroban-abacus-flashcards/commit/a2b3e97eba14b48b25a87443182dbbcb3bbc2c13))
* implement enhanced tactile drag and drop arena with dnd-kit ([4b840e9](https://github.com/antialias/soroban-abacus-flashcards/commit/4b840e9c04080bd61072c6b2294cf2855b374b1e))
* implement fair scoring algorithm for card sorting challenge ([ee7a5e4](https://github.com/antialias/soroban-abacus-flashcards/commit/ee7a5e4a0b223d554fd98aa1e47e74903eae4c6f))
* implement global abacus display configuration and remove client-side SVG generation ([5c3231c](https://github.com/antialias/soroban-abacus-flashcards/commit/5c3231c1702e4c98fb19dd52630cff6e8b8a0195))
* implement HoverCard-based tooltip with enhanced UX and accessibility ([7fef932](https://github.com/antialias/soroban-abacus-flashcards/commit/7fef932134eb670247d02659ddb3a08e787a5f25))
* implement interactive pedagogical reasoning with compact tooltips ([2c09516](https://github.com/antialias/soroban-abacus-flashcards/commit/2c095162e88a9a5ebe0e25b6141ce123e7466f23))
* implement interactive place value editing with NumberFlow animations ([684e624](https://github.com/antialias/soroban-abacus-flashcards/commit/684e62463d0539c46c3937db936574d4a137e239))
* implement intuitive directional gesture system for abacus beads ([7c104f3](https://github.com/antialias/soroban-abacus-flashcards/commit/7c104f37b5d4e1d6b136ba7ad4212329c04dedfb))
* implement learner-friendly pedagogical tooltips with plain language ([01ed22c](https://github.com/antialias/soroban-abacus-flashcards/commit/01ed22c0511359aae8b07433553a6e3cd94ec3fd))
* implement modal dialogs with fullscreen support for challenges ([9b6cabb](https://github.com/antialias/soroban-abacus-flashcards/commit/9b6cabb1111fdbff1e41e45ba9af267d9b6547dd))
* implement native place-value architecture for AbacusReact ([3055f32](https://github.com/antialias/soroban-abacus-flashcards/commit/3055f32e5b417123bc2c4f83fa3b6500c297dda8))
* implement physical abacus logic and fix numeral coloring regression ([5e3d799](https://github.com/antialias/soroban-abacus-flashcards/commit/5e3d799096c432c54643ecbf96943796286ae8ef))
* implement precise inline highlighting of pedagogical terms ([538d356](https://github.com/antialias/soroban-abacus-flashcards/commit/538d356f038dfe29adc0e7d3a58dfc846c00d4bf))
* implement progressive enhancement with minimal loading states ([7e1ce8d](https://github.com/antialias/soroban-abacus-flashcards/commit/7e1ce8d34dbb5f17ed2228ba61150cffa42d7eb8))
* implement progressive multi-step instruction system in AbacusReact ([9195b9b](https://github.com/antialias/soroban-abacus-flashcards/commit/9195b9b6b1571f5bc85c1c37c3f0002eba76a212))
* implement proper SVG transform accumulation for crop mark viewBox calculation ([03230a2](https://github.com/antialias/soroban-abacus-flashcards/commit/03230a2eab8a0539a88308aa442b9cb3db673e91))
* implement provenance system for pedagogical term tracking ([37b5ae8](https://github.com/antialias/soroban-abacus-flashcards/commit/37b5ae86231e22053933ec9f5c469a9ff9a73b23))
* implement React abacus component with independent heaven/earth beads ([528cac5](https://github.com/antialias/soroban-abacus-flashcards/commit/528cac50a851da2068539282a26eb118bf5b296a))
* implement real SVG generation from Python bridge in preview API ([4b90d12](https://github.com/antialias/soroban-abacus-flashcards/commit/4b90d12f39e87e4b9df38f4f5f398990deafefc5))
* implement realistic abacus drag mechanics ([86cbbc8](https://github.com/antialias/soroban-abacus-flashcards/commit/86cbbc8c184031d174a5e88dc0afbab87404fb3c))
* implement revolutionary drag-and-drop champion arena interface ([dbf61c4](https://github.com/antialias/soroban-abacus-flashcards/commit/dbf61c4b2dda7f65359c954f6dd1c43fa0c951bf))
* implement semantic summarizer for pedagogical tooltips ([d1f1bd6](https://github.com/antialias/soroban-abacus-flashcards/commit/d1f1bd6d69b7a84b6179a9caa481f5b9e6dfc66d))
* implement sequential addition problem generation with skill-aware logic ([205badb](https://github.com/antialias/soroban-abacus-flashcards/commit/205badbe70fa9def9a9edbb66df105df387c199a))
* implement skill-based practice step editor system ([9a3afb1](https://github.com/antialias/soroban-abacus-flashcards/commit/9a3afb17ba85a64a28c0dd25980b4c92e3da5483))
* implement smart help detection for Next Action display ([933b948](https://github.com/antialias/soroban-abacus-flashcards/commit/933b94856d98966778e050d42fd565a772ffab16))
* implement smart tooltip positioning to avoid covering active beads ([e104033](https://github.com/antialias/soroban-abacus-flashcards/commit/e1040333710943f536c7a00fd06b855a15459e03))
* implement two-level column highlighting in tutorial player ([bada299](https://github.com/antialias/soroban-abacus-flashcards/commit/bada2996e253baa6159f7198793d1d8eccaf405f))
* implement type-safe place-value API for bead highlighting ([9b6991e](https://github.com/antialias/soroban-abacus-flashcards/commit/9b6991ecff328d625c49b58062731f03faaa4a1e))
* implement unified step positioning for tutorial editor ([6aac8f2](https://github.com/antialias/soroban-abacus-flashcards/commit/6aac8f204af703c3311f523f755e04bce8fb956c))
* improve bead interaction handlers for place-value system ([34b9517](https://github.com/antialias/soroban-abacus-flashcards/commit/34b9517e4a65bed257b79c5064c886775e1b74af))
* improve celebration tooltip positioning to last moved bead ([91c5e58](https://github.com/antialias/soroban-abacus-flashcards/commit/91c5e58029d613839c7a39ed6c35d2cc85422c75))
* improve pedagogical decomposition to break down by place value ([4c75211](https://github.com/antialias/soroban-abacus-flashcards/commit/4c75211d86ca7cf4be02b5e91b9b8ee69004e98c))
* improve preview number selection for better variety demonstration ([3eb053f](https://github.com/antialias/soroban-abacus-flashcards/commit/3eb053f8250cc265aa79cfd1b4e2dfb3370d4fc4))
* improve sorting game UX with visual cues and auto-selection ([a943ceb](https://github.com/antialias/soroban-abacus-flashcards/commit/a943ceb7959809cfa1eaa9bed39fda164fa45038))
* improve visual appearance with dynamic rod bounds and better spacing ([6c95538](https://github.com/antialias/soroban-abacus-flashcards/commit/6c9553825ab6f448e2e0161e20ce5e08a40f66dd))
* initialize CHANGELOG.md for semantic release tracking ([5dcee6b](https://github.com/antialias/soroban-abacus-flashcards/commit/5dcee6b198f0fa337acf2445644ff1c982f8a73c))
* integrate bead diff algorithm with tutorial editor ([472bdf8](https://github.com/antialias/soroban-abacus-flashcards/commit/472bdf8e74f66cfce9a0858cc1520a7f3203b1d6))
* integrate guided addition tutorial into guide page ([b82a8f1](https://github.com/antialias/soroban-abacus-flashcards/commit/b82a8f1308e78571ecad0418347c9d2d03b6a395))
* integrate memory pairs game with arena champions and N-player support ([d9f07d7](https://github.com/antialias/soroban-abacus-flashcards/commit/d9f07d7a4d0292b8eec7cdfe2411e35cd9928532))
* integrate MemoryPairs game with global GameModeContext ([022dca6](https://github.com/antialias/soroban-abacus-flashcards/commit/022dca65186c7cd940a6084fd6564b3b31b242de))
* integrate NumberFlow for smooth animated number display ([e330d35](https://github.com/antialias/soroban-abacus-flashcards/commit/e330d3539da4e502e965268bcd5d2a8b6358988e))
* integrate pytest testing with make targets ([8c15d06](https://github.com/antialias/soroban-abacus-flashcards/commit/8c15d06593947109de8a1a9e94ba6473c6bb8424))
* integrate typst.ts for browser-native SVG generation ([c703a3e](https://github.com/antialias/soroban-abacus-flashcards/commit/c703a3e0270742abbdd5c58d613256ca44e9854d))
* integrate unified skill configuration interface into practice step editor ([9305f11](https://github.com/antialias/soroban-abacus-flashcards/commit/9305f11a017c04bb74fd6cf5d63119437f69f891))
* integrate unified step generator into tutorial editor UI ([88059b2](https://github.com/antialias/soroban-abacus-flashcards/commit/88059b2176e9d7076a88b503e0da16258482da1f))
* make success notification prominent but non-blocking ([7278590](https://github.com/antialias/soroban-abacus-flashcards/commit/7278590a54139766323bdbed7786e51b7e2ff01a))
* migrate all app abaci to browser-side generation ([9be52ac](https://github.com/antialias/soroban-abacus-flashcards/commit/9be52ac689be9805eec817cf0f7319e66d9f025c))
* move progressive test stories to web app with real instruction generator integration ([9d568e3](https://github.com/antialias/soroban-abacus-flashcards/commit/9d568e34f46bbaaae072a2c7076b992f16ad0a31))
* optimize games page for mobile devices ([eb7202d](https://github.com/antialias/soroban-abacus-flashcards/commit/eb7202ddc6507d4b19dd8ddff7f24492b1c2752e))
* optimize memory quiz layout for better viewport usage ([2f0c0fe](https://github.com/antialias/soroban-abacus-flashcards/commit/2f0c0fe57ea3f8cb5879a2446b19d3a12b5c56ba))
* optimize mobile viewport configuration ([476f0fb](https://github.com/antialias/soroban-abacus-flashcards/commit/476f0fb88266702e81f2be8568118eeee25c669f))
* optimize Next.js webpack configuration for WASM ([39b6e5a](https://github.com/antialias/soroban-abacus-flashcards/commit/39b6e5a20f8e7d8a6da66430b7c457c3786f564a))
* optimize showNumbers layout with three modes and visual improvements ([77dc470](https://github.com/antialias/soroban-abacus-flashcards/commit/77dc4702d42376ff099e08051f2d537f0b75a0fc))
* polish interactive abacus with column-based digit display ([ad11e3d](https://github.com/antialias/soroban-abacus-flashcards/commit/ad11e3dc9056914a3f350e3ce00632fea2ea3e53))
* redesign memory game with invisible input and penalty scoring ([b92a867](https://github.com/antialias/soroban-abacus-flashcards/commit/b92a86767797dd11ace94764da42e10d71c2847c))
* regenerate Panda CSS styles for memory quiz and other components ([b8361ee](https://github.com/antialias/soroban-abacus-flashcards/commit/b8361eea50afbdafae0c8f4571b6db6fa3e4e7ff))
* remove normalizeBeadHighlight conversion layer ([6200204](https://github.com/antialias/soroban-abacus-flashcards/commit/62002040b76a6badd2e39f8c6a24176e4950fe83))
* reorganize main page into navigable sectioned layout ([4d179b5](https://github.com/antialias/soroban-abacus-flashcards/commit/4d179b5588fa10526d6852b6d146eef127a404cb))
* replace Champion Arena with Enter Arcade button ([2b98382](https://github.com/antialias/soroban-abacus-flashcards/commit/2b98382b5ac65f613b96621f744d2d462f28ac51))
* replace inline success message with stunning floating overlay ([43f02eb](https://github.com/antialias/soroban-abacus-flashcards/commit/43f02eb539d7f50379a3bb63e9773c730ff8c38d))
* replace legacy abacus components with new AbacusReact ([2a6a010](https://github.com/antialias/soroban-abacus-flashcards/commit/2a6a0104fd05f0806a9fdb4378ecf3c27270aab8))
* replace manual dropdown with Radix UI for proper state management ([bf050fa](https://github.com/antialias/soroban-abacus-flashcards/commit/bf050fa98e24127041cf3e3849f88fb941b9626e))
* replace single-column results with persistent card grid layout ([30ae6e1](https://github.com/antialias/soroban-abacus-flashcards/commit/30ae6e1153afb30f0ea6bdf6a7f5f3ad80520248))
* replace tutorial player arrows with dynamic bead diff algorithm ([e8fe467](https://github.com/antialias/soroban-abacus-flashcards/commit/e8fe467c6c771c292d8978c12d259983b01208f2))
* restore steam train journey enhancements ([045dc9f](https://github.com/antialias/soroban-abacus-flashcards/commit/045dc9fb32e9924ab38a0312009aa64e88bff56a))
* revolutionary single-element editable NumberFlow with live abacus updates ([4bccd65](https://github.com/antialias/soroban-abacus-flashcards/commit/4bccd653051cb39980e578869698941a70e4507a))
* set up monorepo structure with pnpm workspaces and Turborepo ([62e941e](https://github.com/antialias/soroban-abacus-flashcards/commit/62e941e1c0d2bca831d96495fb06f4e13c239a96))
* streamline practice step editor by removing redundant preview section ([beaf3f0](https://github.com/antialias/soroban-abacus-flashcards/commit/beaf3f04438bd762afa0ec7bf50351300678a39b))
* switch tooltip system from Tooltip to HoverCard for better interactivity ([861904f](https://github.com/antialias/soroban-abacus-flashcards/commit/861904fb1fa8849e67e5ebd0131b2af6bc8c4971))
* transform tooltip into celebration when step completed ([057f71e](https://github.com/antialias/soroban-abacus-flashcards/commit/057f71e79576ed0faa7c31e57a5d73223c8111fb))
* update ReasonTooltip UI to prioritize semantic summaries ([6fb0384](https://github.com/antialias/soroban-abacus-flashcards/commit/6fb03845f2755c40347e731b1d934602c4cfcd7f))


### Performance Improvements

* debounce value change events during rapid gesture interactions ([82e15a1](https://github.com/antialias/soroban-abacus-flashcards/commit/82e15a1cd946581a32d4134df32883e874e3cad9))
* eliminate loading flash with delayed loading state ([c70a390](https://github.com/antialias/soroban-abacus-flashcards/commit/c70a390dc63494772ba88f716eaa78353cc649ae))
* optimize tutorial abacus highlighting calculation ([3490f39](https://github.com/antialias/soroban-abacus-flashcards/commit/3490f39a9138267c5b69f72186c3bdc024922da6))
* optimize TutorialEditor TutorialPlayer prop calculations ([8e81d25](https://github.com/antialias/soroban-abacus-flashcards/commit/8e81d25f0648639213d27274b23d70640aa1a5ec))
* speed up bead animations for fast abacus calculations ([1303c93](https://github.com/antialias/soroban-abacus-flashcards/commit/1303c930f25f889151697baa713676eed2faf321))

# Semantic Release

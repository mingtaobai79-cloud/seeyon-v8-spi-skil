# Maven Verification Notes for Generated Seeyon V8 Super SPI Projects

## Positioning
Maven compilation is an optional verification step, not the core function of this skill.

The core function of `seeyon-v8-spi` is to preserve reusable SPI knowledge, route domains, identify contract sources, define generation boundaries, and prevent fake FACTs. Local Maven repositories, IDEA settings, private repository ids, and one-off dependency versions are environment inputs, not reusable defaults.

Do not bake a user's local paths, repository ids, or successful one-off compile configuration into generated examples or skill defaults.

## Trigger
Use this only when the user explicitly asks to compile/verify a generated project, or when they provide enough Maven/private-repository context and want a build result.

If the user is only asking for SPI guidance, documentation, routing, or contract analysis, do not require Maven compilation.

## Required user inputs for compile verification
Before attempting `mvn compile`, collect or discover these as environment-specific inputs:

```yaml
maven:
  executable: <mvn/mvn.cmd absolute path or PATH command>
  settings: <settings.xml path, optional>
  local_repository: <local Maven repo path, optional>
  private_repositories:
    - id: <repository id if known>
      url: <repository URL or local file repository URL>
  offline_allowed: true | false
```

If these are missing, report that compile verification is blocked by environment configuration rather than changing the reusable SPI design.

## Verification levels
Distinguish three levels:

1. Static SPI validation:
   ```bash
   python references/generation/tools/validate_generated_spi_project.py <project-root>
   ```
   This checks structure, module boundaries, registration files, JSON/XML validity, and known SPI-domain guardrails.

2. Maven project validation:
   ```bash
   mvn validate -DskipTests
   ```
   This proves Maven module structure is readable.

3. Java compile verification:
   ```bash
   mvn compile -DskipTests
   ```
   This proves the generated Java skeleton and provided-scope contract jars are usable in the current environment.

Only level 1 is required for skill-level validation. Levels 2/3 are environment-dependent.

## Local repository caveat
A Maven-style local repository copied from another environment may contain `_remote.repositories` markers such as:

```text
artifact.jar>some-private-repo-id=
artifact.pom>some-mirror-id=
```

In that case, `-Dmaven.repo.local=<repo>` may still fail because Maven verifies cached artifacts against currently configured repository ids and may try unrelated remotes.

Generic fix pattern:

1. Ask the user for the Maven executable, settings.xml, local repository path, and private repository ids/URLs.
2. If the repository is a local file repository, create a temporary project-local settings file that maps the relevant ids to the user-provided local repository URL.
3. Run Maven with `-s <temporary-settings.xml>`.
4. Record this in the delivery report as environment verification, not as reusable SPI contract knowledge.

Template shape, with placeholders only:

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 https://maven.apache.org/xsd/settings-1.0.0.xsd">
  <localRepository>${LOCAL_REPOSITORY_PATH}</localRepository>
  <profiles>
    <profile>
      <id>local-private-repos</id>
      <repositories>
        <repository>
          <id>${PRIVATE_REPOSITORY_ID}</id>
          <url>${PRIVATE_REPOSITORY_URL}</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>${PRIVATE_PLUGIN_REPOSITORY_ID}</id>
          <url>${PRIVATE_PLUGIN_REPOSITORY_URL}</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
  <activeProfiles>
    <activeProfile>local-private-repos</activeProfile>
  </activeProfiles>
</settings>
```

## Private facade transitive dependency trap
Some Seeyon facade jars are valid FACT contract jars but their POMs may pull a broad platform dependency tree.

For a generated skeleton that only needs interface/DTO symbols, prefer this rule:

1. Keep the required facade/contract jar as `provided`.
2. Avoid pulling unnecessary transitive dependencies into the generated skeleton.
3. Add only the minimal compile-time `provided` dependency that contains a missing superclass/type.
4. Verify the missing type by scanning the provided jars for the exact `.class` path before naming the dependency.

Do not promote a dependency version discovered from one local environment into a global default. Treat it as FACT only for the reported project/version/locator.

## Reporting rule
Final report must distinguish:

- static validator result,
- optional `mvn validate` result,
- optional `mvn compile` result,
- Maven executable / settings / repository inputs used,
- whether failures are SPI project-structure failures or environment/private dependency resolution failures.

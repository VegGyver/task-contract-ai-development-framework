# Installation and Versioning

The framework is installed once outside all target projects.

## Reference installation

From an extracted release:

```txt
python install.py
tcaf doctor
```

The installer:

- validates the release before installation;
- stores it in a versioned user-level framework directory;
- activates the installed version;
- installs a `tcaf` launcher in the user-level executable directory;
- never copies framework runtime files into a target project.

If the executable directory is not on `PATH`, the installer reports the one environment setup action required by that operating system.

## Upgrade

Run the installer from the newer release. Existing installed versions remain available until intentionally removed.

```txt
tcaf versions
tcaf activate <version>
tcaf doctor
```

Activation changes the runtime version, not project files or project documentation.

## Adapter selection

The order is deterministic:

1. adapter ID supplied by the host integration;
2. `TCAF_ADAPTER`;
3. registered environment detection;
4. `generic-cli`.

Ordinary users do not select internal adapter files. An explicit `--adapter` override exists for adapter development and diagnostics.

## Release policy

- `VERSION`, the central registries, README, changelog and runtime must agree.
- A release is installable only after `tcaf validate` passes.
- A failed acceptance test is corrected within the same architecture.
- An invalid release number is not reused. Version `0.2.8` remains discarded; Architecture A begins at `0.3.0`.

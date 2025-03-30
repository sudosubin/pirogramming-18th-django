{
  description = "sudosubin/pirogramming-18th-django";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable-small";
  };

  outputs = { self, nixpkgs }:
    let
      inherit (nixpkgs.lib) genAttrs platforms;
      forAllSystems = f: genAttrs platforms.unix (system: f (import nixpkgs { inherit system; }));

    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          venvDir = "./.venv";

          buildInputs = with pkgs; [
            python310
            python310Packages.venvShellHook
            poetry
          ];

          postVenvCreation = ''
            poetry install
            poetry run autohooks activate
          '';
        };
      });
    };
}

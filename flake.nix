{
  description = "sudosubin/pirogramming-18th-django";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs { inherit system; };

        in
        {
          devShell = pkgs.mkShell rec {
            venvDir = "./.venv";

            buildInputs = with pkgs; [
              python310
              python310Packages.venvShellHook
            ];

            postVenvCreation = ''
              poetry install
            '';
          };
        }
      );
}

{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [ 
    pkgs.python3 
    pkgs.sudo         # Sudo management.
    pkgs.ffmpeg       # Added ffmpeg package.
  ];

  idx = {
    # Search for the extensions you want on https://open-vsx.org/ using "publisher.id"
    extensions = [ "ms-python.python" ];
    
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file.
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
    };

    # Enable previews and customize configuration.
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "$PORT"; };
          manager = "web";
        };
      };
    };
  };
}

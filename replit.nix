{ pkgs }: {
  deps = [
    pkgs.nginx
    pkgs.geckodriver
    pkgs.openssh
    pkgs.wget
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
    pkgs.python3
  ];
}
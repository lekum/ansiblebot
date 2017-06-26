from errbot import BotPlugin, botcmd
from subprocess import check_output

class AnsibleBot(BotPlugin):
    """Bot that executes Ansible commands remotely"""

    @botcmd
    def ansible(self, msg, args):
        """Run one-time Ansible commands"""
        cmd = " ".join(("ansible", args))
        prefix = "".join(("Executing `ansible ", args, "`:"))
        return "\n".join((prefix, check_output(cmd, shell=True).decode()))

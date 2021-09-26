# -*- coding: utf-8 -*-

import sys

class ModuleManager(object):
    """
    Maya
        Add code to userSetup.py
            ```
            def module_manager_startup():
                from moduleManager import ModuleManager
                global _module_manager
                _module_manager = ModuleManager()

            def module_manager_create_menu():
                module_manager_menu = maya.cmds.menu(
                    "ModuleManagerMenu",
                    label="Module Manager",
                    parent=maya.mel.eval("$retvalue = $gMainWindow;")
                )
                maya.cmds.menuItem(
                    label="Delte non-startup modules",
                    parent=module_manager_menu,
                    command="_module_manager.delete_non_startup_modules()"
                )
                maya.cmds.menuItem(
                    label="Print startup modules",
                    parent=module_manager_menu,
                    command="_module_manager.print_startup_modules()"
                )
                maya.cmds.menuItem(
                    label="Print non-startup modules",
                    parent=module_manager_menu,
                    command="_module_manager.print_non_startup_modules()"
                )
                maya.cmds.menuItem(
                    label="Print loaded modules",
                    parent=module_manager_menu,
                    command="_module_manager.print_loaded_modules()"
                )

            is_batch_mode = maya.cmds.about(batch=True)
            if is_batch_mode is False:
                maya.cmds.evalDeferred(module_manager_startup, lowestPriority=True)
                maya.cmds.evalDeferred(module_manager_create_menu)
            ```
    Nuke
        Add code to init.py
            ```
            def module_manager_startup():
                from moduleManager import ModuleManager
                global _module_manager
                _module_manager = ModuleManager()
            nuke.addOnCreate(module_manager_startup, nodeClass='Root')
            ```
        Add code to menu.py
            ```
            module_manager_menu = nuke.menu("Nuke").addMenu("Module Manager")
            module_manager_menu.addCommand('Delte non-startup modules', '_module_manager.delete_non_startup_modules()')
            module_manager_menu.addCommand('Print startup modules', '_module_manager.print_startup_modules()')
            module_manager_menu.addCommand('Print non-startup modules', '_module_manager.print_non_startup_modules()')
            module_manager_menu.addCommand('Print loaded modules', '_module_manager.print_loaded_modules()')
            ```
    """

    def __init__(self):
        self.startup_modules = sys.modules.keys()

    def delete_non_startup_modules(self):
        for modname in sys.modules.keys():
            if modname not in self.startup_modules:
                del (sys.modules[modname])
    
    def print_startup_modules(self):
        for i, modname in enumerate(self.startup_modules):
            print(i, modname)

    def print_non_startup_modules(self):
        for i, modname in enumerate(sys.modules.keys()):
            if modname not in self.startup_modules:
                print(i, modname)

    def print_loaded_modules(self):
        for i, modname in enumerate(sys.modules.keys()):
            print(i, modname)
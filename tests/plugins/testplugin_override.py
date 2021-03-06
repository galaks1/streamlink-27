from tests.plugins.testplugin import __plugin__ as TestPlugin


class TestPluginOverride(TestPlugin):
    @classmethod
    def bind(cls, *args, **kwargs):
        super(TestPluginOverride, cls).bind(*args, **kwargs)
        cls.module = "testplugin"


__plugin__ = TestPluginOverride

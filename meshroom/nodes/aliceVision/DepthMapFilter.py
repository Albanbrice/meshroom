from meshroom.core import desc

class DepthMapFilter(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'CMPMVS {mvsConfigValue} --filterDepthmap'
    gpu = desc.Level.NORMAL

    mvsConfig = desc.File(
            label='MVS Configuration file',
            description='',
            value='',
            uid=[0],
            isOutput=False,
            )

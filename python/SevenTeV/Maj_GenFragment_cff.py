import FWCore.ParameterSet.Config as cms


generator = cms.EDFilter("Pythia6HadronizerFilter",
            pythiaHepMCVerbosity = cms.untracked.bool(True),
            maxEventsToPrint = cms.untracked.int32(0),
            pythiaPylistVerbosity = cms.untracked.int32(1),
            comEnergy = cms.double(7000.0),
            PythiaParameters = cms.PSet(
            pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
                                           'MSTJ(22)=2     ! Decay those unstable particles',
                                           'PARJ(71)=10 .  ! for which ctau  10 mm',
                                           'MSTP(33)=0     ! no K factors in hard cross sections',
                                           'MSTP(2)=1      ! which order running alphaS',
                                           'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                                           'MSTP(52)=2     ! work with LHAPDF',
                                           'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
                                           'PARP(89)=1800. ! sqrts for which PARP82 is set',
                                           'PARP(90)=0.275 ! Multiple interactions: rescaling power',
                                           'MSTP(95)=6     ! CR (color reconnection parameters)',
                                           'PARP(77)=1.016 ! CR',
                                           'PARP(78)=0.538 ! CR',
                                           'PARP(80)=0.1   ! Prob. colored parton from BBR',
                                           'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
                                           'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
                                           'PARP(62)=1.025 ! ISR cutoff',
                                           'MSTP(91)=1     ! Gaussian primordial kT',
                                           'PARP(93)=10.0  ! primordial kT-max',
                                           'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
                                           'MSTP(82)=4     ! Defines the multi-parton model'),
                    processParameters = cms.vstring('MSEL=0         ! User defined processes',
                                                    'PMAS(5,1)=4.8   ! b quark mass',
                                                    'PMAS(6,1)=172.5 ! t quark mass',
                                                    'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
                                                    'MSTP(61)=1      ! Parton showering on or off'),
                    parameterSets = cms.vstring('pythiaUESettings',
                                                'processParameters')
            )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    name = cms.untracked.string('$Maj_GenFragment_cff.py,v $'),
    annotation = cms.untracked.string('Majorana neutrino 7TeV')
            )


Release notes
=============

v0.5.0
------

Bug fixes

  - `#371`_ preserve integer hop lengths in constant-Q transforms. *Brian McFee*
  - `#386`_ fixed a length check in ``librosa.util.frame``. *Brian McFee*
  - `#416`_ ``librosa.output.write_wav`` only normalizes floating point, and normalization is disabled by
    default. *Brian McFee*
  - `#417`_ ``librosa.cqt`` output is now scaled continuously across octave boundaries. *Brian McFee, Eric
    Humphrey*
  - `#450`_ enhanced numerical stability for ``librosa.util.softmask``. *Brian McFee*
  - `#467`_ correction to chroma documentation. *Seth Kranzler*
  - `#501`_ fixed a numpy 1.12 compatibility error in ``pitch_tuning``. *Hojin Lee*

New features

  - `#323`_ ``librosa.dtw`` dynamic time warping. *Stefan Balke*
  - `#404`_ ``librosa.cache`` now supports priority levels, analogous to logging levels. *Brian McFee*
  - `#405`_ ``librosa.interp_harmonics`` for estimating harmonics of time-frequency representations. *Brian
    McFee*
  - `#410`_ ``librosa.beat.beat_track`` and ``librosa.onset.onset_detect`` can return output in frames,
    samples, or time units. *Brian McFee*
  - `#413`_ full support for scipy-style window specifications. *Brian McFee*
  - `#427`_ ``librosa.salience`` for computing spectrogram salience using harmonic peaks. *Rachel Bittner*
  - `#428`_ ``librosa.effects.trim`` and ``librosa.effects.split`` for trimming and splitting waveforms. *Brian
    McFee*
  - `#464`_ ``librosa.amplitude_to_db``, ``db_to_amplitude``, ``power_to_db``, and ``db_to_power`` for
    amplitude conversions.  This deprecates ``logamplitude``.  *Brian McFee*
  - `#471`_ ``librosa.util.normalize`` now supports ``threshold`` and ``fill_value`` arguments. *Brian McFee*
  - `#472`_ ``librosa.feature.melspectrogram`` now supports ``power`` argument. *Keunwoo Choi*
  - `#473`_ ``librosa.onset.onset_backtrack`` for backtracking onset events to previous local minima of
    energy. *Brian McFee*
  - `#479`_ ``librosa.beat.tempo`` replaces ``librosa.beat.estimate_tempo``, supports time-varying estimation.
    *Brian McFee*
  

Other changes

  - `#352`_ removed ``seaborn`` integration. *Brian McFee*
  - `#368`_ rewrite of the ``librosa.display`` submodule.  All plots are now in natural coordinates. *Brian
    McFee*
  - `#402`_ ``librosa.display`` submodule is not automatically imported. *Brian McFee*
  - `#403`_ ``librosa.decompose.hpss`` now returns soft masks. *Brian McFee*
  - `#407`_ ``librosa.feature.rmse`` can now compute directly in the time domain. *Carl Thome*
  - `#432`_ ``librosa.feature.rmse`` renames ``n_fft`` to ``frame_length``. *Brian McFee*
  - `#446`_ ``librosa.cqt`` now disables tuning estimation by default. *Brian McFee*
  - `#452`_ ``librosa.filters.__float_window`` now always uses integer length windows. *Brian McFee*
  - `#459`_ ``librosa.load`` now supports ``res_type`` argument for resampling. *CJ Carr*
  - `#482`_ ``librosa.filters.mel`` now warns if parameters will generate empty filter channels. *Brian McFee*
  - `#480`_ expanded documentation for advanced IO use-cases. *Fabian Robert-Stoeter*

API changes and compatibility

  - The following functions have permanently moved:
        - ``core.peak_peak`` to ``util.peak_pick``
        - ``core.localmax`` to ``util.localmax``
        - ``feature.sync`` to ``util.sync``

  - The following functions, classes, and constants have been removed:
        - ``core.ifptrack``
        - ``feature.chromagram``
        - ``feature.logfsgram``
        - ``filters.logfrequency``
        - ``output.frames_csv``
        - ``segment.structure_Feature``
        - ``display.time_ticks``
        - ``util.FeatureExtractor``
        - ``util.buf_to_int``
        - ``util.SMALL_FLOAT``

  - The following parameters have been removed:
        - ``librosa.cqt``: `resolution`
        - ``librosa.cqt``: `aggregate`
        - ``feature.chroma_cqt``: `mode`
        - ``onset_strength``: `centering`

  - Seaborn integration has been removed, and the ``display`` submodule now requires matplotlib >= 1.5.
        - The `use_sns` argument has been removed from `display.cmap`
        - `magma` is now the default sequential colormap.

  - The ``librosa.display`` module has been rewritten.
        - ``librosa.display.specshow`` now plots using `pcolormesh`, and supports non-uniform time and frequency axes.
        - All plots can be rendered in natural coordinates (e.g., time or Hz)
        - Interactive plotting is now supported via ticker and formatter objects

  - ``librosa.decompose.hpss`` with `mask=True` now returns soft masks, rather than binary masks.

  - ``librosa.filters.get_window`` wraps ``scipy.signal.get_window``, and handles generic callables as well pre-registered
    window functions.  All windowed analyses (e.g., ``stft``, ``cqt``, or ``tempogram``) now support the full range
    of window functions and parameteric windows via tuple parameters, e.g., ``window=('kaiser', 4.0)``.
        
  - ``stft`` windows are now explicitly asymmetric by default, which breaks backwards compatibility with the 0.4 series.

  - ``cqt`` now returns properly scaled outputs that are continuous across octave boundaries.  This breaks
    backwards compatibility with the 0.4 series.

  - ``cqt`` now uses `tuning=0.0` by default, rather than estimating the tuning from the signal.  Tuning
    estimation is still supported, and enabled by default for chroma analysis (``librosa.feature.chroma_cqt``).

  - ``logamplitude`` is deprecated in favor of ``amplitude_to_db`` or ``power_to_db``.  The `ref_power` parameter
    has been renamed to `ref`.


.. _#501: https://github.com/librosa/librosa/pull/501
.. _#480: https://github.com/librosa/librosa/pull/480
.. _#467: https://github.com/librosa/librosa/pull/467
.. _#450: https://github.com/librosa/librosa/pull/450
.. _#417: https://github.com/librosa/librosa/pull/417
.. _#416: https://github.com/librosa/librosa/pull/416
.. _#386: https://github.com/librosa/librosa/pull/386
.. _#371: https://github.com/librosa/librosa/pull/371
.. _#479: https://github.com/librosa/librosa/pull/479
.. _#473: https://github.com/librosa/librosa/pull/473
.. _#472: https://github.com/librosa/librosa/pull/472
.. _#471: https://github.com/librosa/librosa/pull/471
.. _#464: https://github.com/librosa/librosa/pull/464
.. _#428: https://github.com/librosa/librosa/pull/428
.. _#427: https://github.com/librosa/librosa/pull/427
.. _#413: https://github.com/librosa/librosa/pull/413
.. _#410: https://github.com/librosa/librosa/pull/410
.. _#405: https://github.com/librosa/librosa/pull/405
.. _#404: https://github.com/librosa/librosa/pull/404
.. _#323: https://github.com/librosa/librosa/pull/323
.. _#482: https://github.com/librosa/librosa/pull/482
.. _#459: https://github.com/librosa/librosa/pull/459
.. _#452: https://github.com/librosa/librosa/pull/452
.. _#446: https://github.com/librosa/librosa/pull/446
.. _#432: https://github.com/librosa/librosa/pull/432
.. _#407: https://github.com/librosa/librosa/pull/407
.. _#403: https://github.com/librosa/librosa/pull/403
.. _#402: https://github.com/librosa/librosa/pull/402
.. _#368: https://github.com/librosa/librosa/pull/368
.. _#352: https://github.com/librosa/librosa/pull/352



v0.4.3
------
2016-05-17

Bug fixes
  - `#315`_ fixed a positioning error in ``display.specshow`` with logarithmic axes. *Brian McFee*
  - `#332`_ ``librosa.cqt`` now throws an exception if the signal is too short for analysis. *Brian McFee*
  - `#341`_ ``librosa.hybrid_cqt`` properly matches the scale of ``librosa.cqt``. *Brian McFee*
  - `#348`_ ``librosa.cqt`` fixed a bug introduced in v0.4.2. *Brian McFee*
  - `#354`_ Fixed a minor off-by-one error in ``librosa.beat.estimate_tempo``. *Brian McFee*
  - `#357`_ improved numerical stability of ``librosa.decompose.hpss``. *Brian McFee*

New features
  - `#312`_ ``librosa.segment.recurrence_matrix`` can now construct sparse self-similarity matrices. *Brian
    McFee*
  - `#337`_ ``librosa.segment.recurrence_matrix`` can now produce weighted affinities and distances. *Brian
    McFee*
  - `#311`_ ``librosa.decompose.nl_filter`` implements several self-similarity based filtering operations
    including non-local means. *Brian McFee*
  - `#320`_ ``librosa.feature.chroma_cens`` implements chroma energy normalized statistics (CENS) features.
    *Stefan Balke*
  - `#354`_ ``librosa.core.tempo_frequencies`` computes tempo (BPM) frequencies for autocorrelation and
    tempogram features. *Brian McFee*
  - `#355`_ ``librosa.decompose.hpss`` now supports harmonic-percussive-residual separation. *CJ Carr, Brian McFee*
  - `#357`_ ``librosa.util.softmask`` computes numerically stable soft masks. *Brian McFee*

Other changes
  - ``librosa.cqt``, ``librosa.hybrid_cqt`` parameter `aggregate` is now deprecated.
  - Resampling is now handled by the ``resampy`` library
  - ``librosa.get_duration`` can now operate directly on filenames as well as audio buffers and feature
    matrices.
  - ``librosa.decompose.hpss`` no longer supports ``power=0``.

.. _#315: https://github.com/librosa/librosa/pull/315
.. _#332: https://github.com/librosa/librosa/pull/332
.. _#341: https://github.com/librosa/librosa/pull/341
.. _#348: https://github.com/librosa/librosa/pull/348
.. _#312: https://github.com/librosa/librosa/pull/312
.. _#337: https://github.com/librosa/librosa/pull/337
.. _#311: https://github.com/librosa/librosa/pull/311
.. _#320: https://github.com/librosa/librosa/pull/320
.. _#354: https://github.com/librosa/librosa/pull/354
.. _#355: https://github.com/librosa/librosa/pull/355
.. _#357: https://github.com/librosa/librosa/pull/357

v0.4.2
------
2016-02-20

Bug fixes
  - Support for matplotlib 1.5 color properties in the ``display`` module
  - `#308`_ Fixed a per-octave scaling error in ``librosa.cqt``. *Brian McFee*

New features
  - `#279`_ ``librosa.cqt`` now provides complex-valued output with argument `real=False`.
    This will become the default behavior in subsequent releases.
  - `#288`_ ``core.resample`` now supports multi-channel inputs. *Brian McFee*
  - `#295`_ ``librosa.display.frequency_ticks``: like ``time_ticks``. Ticks can now dynamically
    adapt to scale (mHz, Hz, KHz, MHz, GHz) and use automatic precision formatting (``%g``). *Brian McFee*


Other changes
  - `#277`_ improved documentation for OSX. *Stefan Balke*
  - `#294`_ deprecated the ``FeatureExtractor`` object. *Brian McFee*
  - `#300`_ added dependency version requirements to install script. *Brian McFee*
  - `#302`_, `#279`_ renamed the following parameters
      - ``librosa.display.time_ticks``: `fmt` is now `time_fmt`
      - ``librosa.feature.chroma_cqt``: `mode` is now `cqt_mode`
      - ``librosa.cqt``, ``hybrid_cqt``, ``pseudo_cqt``, ``librosa.filters.constant_q``: `resolution` is now `filter_scale`
  - `#308`_ ``librosa.cqt`` default `filter_scale` parameter is now 1 instead of 2.

.. _#277: https://github.com/librosa/librosa/pull/277
.. _#279: https://github.com/librosa/librosa/pull/279
.. _#288: https://github.com/librosa/librosa/pull/288
.. _#294: https://github.com/librosa/librosa/pull/294
.. _#295: https://github.com/librosa/librosa/pull/295
.. _#300: https://github.com/librosa/librosa/pull/300
.. _#302: https://github.com/librosa/librosa/pull/302
.. _#308: https://github.com/librosa/librosa/pull/308

v0.4.1
------
2015-10-17

Bug fixes
  - Improved safety check in CQT for invalid hop lengths
  - Fixed division by zero bug in ``core.pitch.pip_track``
  - Fixed integer-type error in ``util.pad_center`` on numpy v1.10
  - Fixed a context scoping error in ``librosa.load`` with some audioread backends
  - ``librosa.autocorrelate`` now persists type for complex input

New features
  - ``librosa.clicks`` sonifies timed events such as beats or onsets
  - ``librosa.onset.onset_strength_multi`` computes onset strength within multiple sub-bands
  - ``librosa.feature.tempogram`` computes localized onset strength autocorrelation
  - ``librosa.display.specshow`` now supports ``*_axis='tempo'`` for annotating tempo-scaled data
  - ``librosa.fmt`` implements the Fast Mellin Transform

Other changes

  - Rewrote ``display.waveplot`` for improved efficiency
  - ``decompose.deompose()`` now supports pre-trained transformation objects
  - Nullified side-effects of optional seaborn dependency
  - Moved ``feature.sync`` to ``util.sync`` and expanded its functionality
  - ``librosa.onset.onset_strength`` and ``onset_strength_multi`` support superflux-style lag and max-filtering
  - ``librosa.core.autocorrelate`` can now operate along any axis of multi-dimensional input
  - the ``segment`` module functions now support arbitrary target axis
  - Added proper window normalization to ``librosa.core.istft`` for better reconstruction 
    (`PR #235 <https://github.com/librosa/librosa/pull/235>`_).
  - Standardized ``n_fft=2048`` for ``piptrack``, ``ifptrack`` (deprecated), and
    ``logfsgram`` (deprecated)
  - ``onset_strength`` parameter ``'centering'`` has been deprecated and renamed to
    ``'center'``
  - ``onset_strength`` always trims to match the input spectrogram duration
  - added tests for ``piptrack``
  - added test support for Python 3.5




v0.4.0
------
2015-07-08

Bug fixes

-  Fixed alignment errors with ``offset`` and ``duration`` in ``load()``
-  Fixed an edge-padding issue with ``decompose.hpss()`` which resulted
   in
   percussive noise leaking into the harmonic component.
-  Fixed stability issues with ``ifgram()``, added options to suppress
   negative frequencies.
-  Fixed scaling and padding errors in ``feature.delta()``
-  Fixed some errors in ``note_to_hz()`` string parsing
-  Added robust range detection for ``display.cmap``
-  Fixed tick placement in ``display.specshow``
-  Fixed a low-frequency filter alignment error in ``cqt``
-  Added aliasing checks for ``cqt`` filterbanks
-  Fixed corner cases in ``peak_pick``
-  Fixed bugs in ``find_files()`` with negative slicing
-  Fixed tuning estimation errors
-  Fixed octave numbering in to conform to scientific pitch notation

New features

-  python 3 compatibility
-  Deprecation and moved-function warnings
-  added ``norm=None`` option to ``util.normalize()``
-  ``segment.recurrence_to_lag``, ``lag_to_recurrence``
-  ``core.hybrid_cqt()`` and ``core.pseudo_cqt()``
-  ``segment.timelag_filter``
-  Efficiency enhancements for ``cqt``
-  Major rewrite and reformatting of documentation
-  Improvements to ``display.specshow``:

   -  added the ``lag`` axis format
   -  added the ``tonnetz`` axis format
   -  allow any combination of axis formats

-  ``effects.remix()``
-  Added new time and frequency converters:

   -  ``note_to_hz()``, ``hz_to_note()``
   -  ``frames_to_samples()``, ``samples_to_frames()``
   -  ``time_to_samples()``, ``samples_to_time()``

-  ``core.zero_crossings``
-  ``util.match_events()``
-  ``segment.subsegment()`` for segmentation refinement
-  Functional examples in almost all docstrings
-  improved numerical stability in ``normalize()``
-  audio validation checks
-  ``to_mono()``
-  ``librosa.cache`` for storing pre-computed features
-  Stereo output support in ``write_wav``
-  Added new feature extraction functions:

   -  ``feature.spectral_contrast``
   -  ``feature.spectral_bandwidth``
   -  ``feature.spectral_centroid``
   -  ``feature.spectral_rolloff``
   -  ``feature.poly_features``
   -  ``feature.rmse``
   -  ``feature.zero_crossing_rate``
   -  ``feature.tonnetz``

- Added ``display.waveplot``

Other changes

-  Internal refactoring and restructuring of submodules
-  Removed the ``chord`` module
-  input validation and better exception reporting for most functions
-  Changed the default colormaps in ``display``
-  Changed default parameters in onset detection, beat tracking
-  Changed default parameters in ``cqt``
-  ``filters.constant_q`` now returns filter lengths
-  Chroma now starts at ``C`` by default, instead of ``A``
-  ``pad_center`` supports multi-dimensional input and ``axis``
   parameter
- switched from ``np.fft`` to ``scipy.fftpack`` for FFT operations
- changed all librosa-generated exception to a new class librosa.ParameterError

Deprecated functions

-  ``util.buf_to_int``
-  ``output.frames_csv``
-  ``segment.structure_feature``
-  ``filters.logfrequency``
-  ``feature.logfsgram``

v0.3.1
------
2015-02-18

Bug fixes

-  Fixed bug #117: ``librosa.segment.agglomerative`` now returns a
   numpy.ndarray instead of a list
-  Fixed bug #115: off-by-one error in ``librosa.core.load`` with fixed
   duration
-  Fixed numerical underflow errors in ``librosa.decompose.hpss``
-  Fixed bug #104: ``librosa.decompose.hpss`` failed with silent,
   complex-valued input
-  Fixed bug #103: ``librosa.feature.estimate_tuning`` fails when no
   bins exceed the threshold

Features

-  New function ``librosa.core.get_duration()`` computes the duration of
   an audio signal
   or spectrogram-like input matrix
-  ``librosa.util.pad_center`` now accepts multi-dimensional input

Other changes

-  Adopted the ISC license
-  Python 3 compatibility via futurize
-  Fixed issue #102: segment.agglomerative no longer depends on the
   deprecated
   Ward module of sklearn; it now depends on the newer Agglomerative
   module.
-  Issue #108: set character encoding on all source files
-  Added dtype persistence for resample, stft, istft, and effects
   functions

v0.3.0
------
2014-06-30

Bug fixes

-  Fixed numpy array indices to force integer values
-  ``librosa.util.frame`` now warns if the input data is non-contiguous
-  Fixed a formatting error in ``librosa.display.time_ticks()``
-  Added a warning if ``scikits.samplerate`` is not detected

Features

-  New module ``librosa.chord`` for training chord recognition models
-  Parabolic interpolation piptracking ``librosa.feature.piptrack()``
-  ``librosa.localmax()`` now supports multi-dimensional slicing
-  New example scripts
-  Improved documentation
-  Added the ``librosa.util.FeatureExtractor`` class, which allows
   librosa functions
   to act as feature extraction stages in ``sklearn``
-  New module ``librosa.effects`` for time-domain audio processing
-  Added demo notebooks for the ``librosa.effects`` and
   ``librosa.util.FeatureExtractor``
-  Added a full-track audio example,
   ``librosa.util.example_audio_file()``
-  Added peak-frequency sorting of basis elements in
   ``librosa.decompose.decompose()``

Other changes

-  Spectrogram frames are now centered, rather than left-aligned. This
   removes the
   need for window correction in ``librosa.frames_to_time()``
-  Accelerated constant-Q transform ``librosa.cqt()``
-  PEP8 compliance
-  Removed normalization from ``librosa.feature.logfsgram()``
-  Efficiency improvements by ensuring memory contiguity
-  ``librosa.logamplitude()`` now supports functional reference power,
   in addition
   to scalar values
-  Improved ``librosa.feature.delta()``
-  Additional padding options to ``librosa.feature.stack_memory()``
-  ``librosa.cqt`` and ``librosa.feature.logfsgram`` now use the same
   parameter
   formats ``(fmin, n_bins, bins_per_octave)``.
-  Updated demo notebook(s) to IPython 2.0
-  Moved ``perceptual_weighting()`` from ``librosa.feature`` into
   ``librosa.core``
-  Moved ``stack_memory()`` from ``librosa.segment`` into
   ``librosa.feature``
-  Standardized ``librosa.output.annotation`` input format to match
   ``mir_eval``
-  Standardized variable names (e.g., ``onset_envelope``).

v0.2.1
------
2014-01-21

Bug fixes

-  fixed an off-by-one error in ``librosa.onset.onset_strength()``
-  fixed a sign-flip error in ``librosa.output.write_wav()``
-  removed all mutable object default parameters

Features

-  added option ``centering`` to ``librosa.onset.onset_strength()`` to
   resolve frame-centering issues with sliding window STFT
-  added frame-center correction to ``librosa.core.frames_to_time()``
   and ``librosa.core.time_to_frames()``
-  added ``librosa.util.pad_center()``
-  added ``librosa.output.annotation()``
-  added ``librosa.output.times_csv()``
-  accelerated ``librosa.core.stft()`` and ``ifgram()``
-  added ``librosa.util.frame`` for in-place signal framing
-  ``librosa.beat.beat_track`` now supports user-supplied tempo
-  added ``librosa.util.normalize()``
-  added ``librosa.util.find_files()``
-  added ``librosa.util.axis_sort()``
-  new module: ``librosa.util()``
-  ``librosa.filters.constant_q`` now support padding
-  added boolean input support for ``librosa.display.cmap()``
-  speedup in ``librosa.core.cqt()``

Other changes

-  optimized default parameters for ``librosa.onset.onset_detect``
-  set ``librosa.filters.mel`` parameter ``n_mels=128`` by default
-  ``librosa.feature.chromagram()`` and ``logfsgram()`` now use power
   instead of energy
-  ``librosa.display.specshow()`` with ``y_axis='chroma'`` now labels as
   ``pitch class``
-  set ``librosa.core.cqt`` parameter ``resolution=2`` by default
-  set ``librosa.feature.chromagram`` parameter ``octwidth=2`` by
   default

v0.2.0
------
2013-12-14

Bug fixes

-  fixed default ``librosa.core.stft, istft, ifgram`` to match
   specification
-  fixed a float->int bug in peak\_pick
-  better memory efficiency
-  ``librosa.segment.recurrence_matrix`` corrects for width suppression
-  fixed a divide-by-0 error in the beat tracker
-  fixed a bug in tempo estimation with short windows
-  ``librosa.feature.sync`` now supports 1d arrays
-  fixed a bug in beat trimming
-  fixed a bug in ``librosa.core.stft`` when calculating window size
-  fixed ``librosa.core.resample`` to support stereo signals

Features

-  added filters option to cqt
-  added window function support to istft
-  added an IPython notebook demo
-  added ``librosa.features.delta`` for computing temporal difference
   features
-  new ``examples`` scripts: tuning, hpss
-  added optional trimming to ``librosa.segment.stack_memory``
-  ``librosa.onset.onset_strength`` now takes generic spectrogram
   function ``feature``
-  compute reference power directly in ``librosa.core.logamplitude``
-  color-blind-friendly default color maps in ``librosa.display.cmap``
-  ``librosa.core.onset_strength`` now accepts an aggregator
-  added ``librosa.feature.perceptual_weighting``
-  added tuning estimation to ``librosa.feature.chromagram``
-  added ``librosa.core.A_weighting``
-  vectorized frequency converters
-  added ``librosa.core.cqt_frequencies`` to get CQT frequencies
-  ``librosa.core.cqt`` basic constant-Q transform implementation
-  ``librosa.filters.cq_to_chroma`` to convert log-frequency to chroma
-  added ``librosa.core.fft_frequencies``
-  ``librosa.decompose.hpss`` can now return masking matrices
-  added reversal for ``librosa.segment.structure_feature``
-  added ``librosa.core.time_to_frames``
-  added cent notation to ``librosa.core.midi_to_note``
-  added time-series or spectrogram input options to ``chromagram``,
   ``logfsgram``, ``melspectrogram``, and ``mfcc``
-  new module: ``librosa.display``
-  ``librosa.output.segment_csv`` => ``librosa.output.frames_csv``
-  migrated frequency converters to ``librosa.core``
-  new module: ``librosa.filters``
-  ``librosa.decompose.hpss`` now supports complex-valued STFT matrices
-  ``librosa.decompose.decompose()`` supports ``sklearn`` decomposition
   objects
-  added ``librosa.core.phase_vocoder``
-  new module: ``librosa.onset``; migrated onset strength from
   ``librosa.beat``
-  added ``librosa.core.pick_peaks``
-  ``librosa.core.load()`` supports offset and duration parameters
-  ``librosa.core.magphase()`` to separate magnitude and phase from a
   complex matrix
-  new module: ``librosa.segment``

Other changes

-  ``onset_estimate_bpm => estimate_tempo``
-  removed ``n_fft`` from ``librosa.core.istft()``
-  ``librosa.core.mel_frequencies`` returns ``n_mels`` values by default
-  changed default ``librosa.decompose.hpss`` window to 31
-  disabled onset de-trending by default in
   ``librosa.onset.onset_strength``
-  added complex-value warning to ``librosa.display.specshow``
-  broke compatibilty with ``ifgram.m``; ``librosa.core.ifgram`` now
   matches ``stft``
-  changed default beat tracker settings
-  migrated ``hpss`` into ``librosa.decompose``
-  changed default ``librosa.decompose.hpss`` power parameter to ``2.0``
-  ``librosa.core.load()`` now returns single-precision by default
-  standardized ``n_fft=2048``, ``hop_length=512`` for most functions
-  refactored tempo estimator

v0.1.0
------

Initial public release.

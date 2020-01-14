from __clrclasses__.System import ICloneable as _n_0_t_0
from __clrclasses__.System import Array as _n_0_t_1
from __clrclasses__.System import DateTime as _n_0_t_2
from __clrclasses__.System import DayOfWeek as _n_0_t_3
from __clrclasses__.System import Enum as _n_0_t_4
from __clrclasses__.System import IComparable as _n_0_t_5
from __clrclasses__.System import IFormattable as _n_0_t_6
from __clrclasses__.System import IConvertible as _n_0_t_7
from __clrclasses__.System import Char as _n_0_t_8
from __clrclasses__.System import IFormatProvider as _n_0_t_9
from __clrclasses__.System import ArgumentException as _n_0_t_10
from __clrclasses__.System import Nullable as _n_0_t_11
from __clrclasses__.System import Exception as _n_0_t_12
from __clrclasses__.System import TimeSpan as _n_0_t_13
from __clrclasses__.System import StringComparer as _n_0_t_14
from __clrclasses__.System import Byte as _n_0_t_15
from __clrclasses__.System import IEquatable as _n_0_t_16
from __clrclasses__.System import Guid as _n_0_t_17
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_0
from __clrclasses__.System.Reflection import Assembly as _n_2_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_3_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_4_t_1
import typing
class Calendar(_n_0_t_0):
    CurrentEra: int
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:"""AlgorithmType { get; } -> CalendarAlgorithmType"""
    @property
    def Eras(self) -> _n_0_t_1[int]:"""Eras { get; } -> Array"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def MaxSupportedDateTime(self) -> _n_0_t_2:"""MaxSupportedDateTime { get; } -> DateTime"""
    @property
    def MinSupportedDateTime(self) -> _n_0_t_2:"""MinSupportedDateTime { get; } -> DateTime"""
    @property
    def TwoDigitYearMax(self) -> int:"""TwoDigitYearMax { get; set; } -> int"""
    def AddDays(self, time: _n_0_t_2, days: int) -> _n_0_t_2:...
    def AddHours(self, time: _n_0_t_2, hours: int) -> _n_0_t_2:...
    def AddMilliseconds(self, time: _n_0_t_2, milliseconds: float) -> _n_0_t_2:...
    def AddMinutes(self, time: _n_0_t_2, minutes: int) -> _n_0_t_2:...
    def AddMonths(self, time: _n_0_t_2, months: int) -> _n_0_t_2:...
    def AddSeconds(self, time: _n_0_t_2, seconds: int) -> _n_0_t_2:...
    def AddWeeks(self, time: _n_0_t_2, weeks: int) -> _n_0_t_2:...
    def AddYears(self, time: _n_0_t_2, years: int) -> _n_0_t_2:...
    def GetDayOfMonth(self, time: _n_0_t_2) -> int:...
    def GetDayOfWeek(self, time: _n_0_t_2) -> _n_0_t_3:...
    def GetDayOfYear(self, time: _n_0_t_2) -> int:...
    def GetDaysInMonth(self, year: int, month: int, era: int) -> int:...
    def GetDaysInMonth(self, year: int, month: int) -> int:...
    def GetDaysInYear(self, year: int, era: int) -> int:...
    def GetDaysInYear(self, year: int) -> int:...
    def GetEra(self, time: _n_0_t_2) -> int:...
    def GetHour(self, time: _n_0_t_2) -> int:...
    def GetLeapMonth(self, year: int, era: int) -> int:...
    def GetLeapMonth(self, year: int) -> int:...
    def GetMilliseconds(self, time: _n_0_t_2) -> float:...
    def GetMinute(self, time: _n_0_t_2) -> int:...
    def GetMonth(self, time: _n_0_t_2) -> int:...
    def GetMonthsInYear(self, year: int, era: int) -> int:...
    def GetMonthsInYear(self, year: int) -> int:...
    def GetSecond(self, time: _n_0_t_2) -> int:...
    def GetWeekOfYear(self, time: _n_0_t_2, rule: CalendarWeekRule, firstDayOfWeek: _n_0_t_3) -> int:...
    def GetYear(self, time: _n_0_t_2) -> int:...
    def IsLeapDay(self, year: int, month: int, day: int, era: int) -> bool:...
    def IsLeapDay(self, year: int, month: int, day: int) -> bool:...
    def IsLeapMonth(self, year: int, month: int, era: int) -> bool:...
    def IsLeapMonth(self, year: int, month: int) -> bool:...
    def IsLeapYear(self, year: int, era: int) -> bool:...
    def IsLeapYear(self, year: int) -> bool:...
    @staticmethod
    def ReadOnly(calendar: Calendar) -> Calendar:...
    def ToDateTime(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> _n_0_t_2:...
    def ToDateTime(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> _n_0_t_2:...
    def ToFourDigitYear(self, year: int) -> int:...
class CalendarAlgorithmType(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    LunarCalendar: int
    LunisolarCalendar: int
    SolarCalendar: int
    Unknown: int
    value__: int
class CalendarWeekRule(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    FirstDay: int
    FirstFourDayWeek: int
    FirstFullWeek: int
    value__: int
class CharUnicodeInfo(object):
    @staticmethod
    def GetDecimalDigitValue(s: str, index: int) -> int:...
    @staticmethod
    def GetDecimalDigitValue(ch: _n_0_t_8) -> int:...
    @staticmethod
    def GetDigitValue(s: str, index: int) -> int:...
    @staticmethod
    def GetDigitValue(ch: _n_0_t_8) -> int:...
    @staticmethod
    def GetNumericValue(s: str, index: int) -> float:...
    @staticmethod
    def GetNumericValue(ch: _n_0_t_8) -> float:...
    @staticmethod
    def GetUnicodeCategory(s: str, index: int) -> UnicodeCategory:...
    @staticmethod
    def GetUnicodeCategory(ch: _n_0_t_8) -> UnicodeCategory:...
class ChineseLunisolarCalendar(EastAsianLunisolarCalendar, _n_0_t_0):
    ChineseEra: int
    def __init__(self) -> ChineseLunisolarCalendar:...
class CompareInfo(_n_4_t_0):
    @property
    def LCID(self) -> int:"""LCID { get; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Version(self) -> SortVersion:"""Version { get; } -> SortVersion"""
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int) -> int:...
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int, options: CompareOptions) -> int:...
    def Compare(self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int) -> int:...
    def Compare(self, string1: str, string2: str, options: CompareOptions) -> int:...
    def Compare(self, string1: str, string2: str) -> int:...
    def Compare(self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int, options: CompareOptions) -> int:...
    @staticmethod
    def GetCompareInfo(name: str) -> CompareInfo:...
    @staticmethod
    def GetCompareInfo(culture: int) -> CompareInfo:...
    @staticmethod
    def GetCompareInfo(name: str, assembly: _n_2_t_0) -> CompareInfo:...
    @staticmethod
    def GetCompareInfo(culture: int, assembly: _n_2_t_0) -> CompareInfo:...
    def GetSortKey(self, source: str) -> SortKey:...
    def GetSortKey(self, source: str, options: CompareOptions) -> SortKey:...
    def IndexOf(self, source: str, value: str, startIndex: int, count: int, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8, startIndex: int, count: int, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8, startIndex: int, count: int) -> int:...
    def IndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8, startIndex: int, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: str, startIndex: int) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8, startIndex: int) -> int:...
    def IndexOf(self, source: str, value: str, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8, options: CompareOptions) -> int:...
    def IndexOf(self, source: str, value: str) -> int:...
    def IndexOf(self, source: str, value: _n_0_t_8) -> int:...
    def IsPrefix(self, source: str, prefix: str) -> bool:...
    def IsPrefix(self, source: str, prefix: str, options: CompareOptions) -> bool:...
    @staticmethod
    def IsSortable(text: str) -> bool:...
    @staticmethod
    def IsSortable(ch: _n_0_t_8) -> bool:...
    def IsSuffix(self, source: str, suffix: str) -> bool:...
    def IsSuffix(self, source: str, suffix: str, options: CompareOptions) -> bool:...
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8, startIndex: int, count: int, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8, startIndex: int, count: int) -> int:...
    def LastIndexOf(self, source: str, value: str, startIndex: int, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8, startIndex: int, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: str, startIndex: int) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8, startIndex: int) -> int:...
    def LastIndexOf(self, source: str, value: str, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8, options: CompareOptions) -> int:...
    def LastIndexOf(self, source: str, value: str) -> int:...
    def LastIndexOf(self, source: str, value: _n_0_t_8) -> int:...
    def GetStringComparer(self, options: CompareOptions) -> _n_0_t_14:
        """Extension from: System.Globalization.GlobalizationExtensions"""
class CompareOptions(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    IgnoreCase: int
    IgnoreKanaType: int
    IgnoreNonSpace: int
    IgnoreSymbols: int
    IgnoreWidth: int
    _None: int
    Ordinal: int
    OrdinalIgnoreCase: int
    StringSort: int
    value__: int
class CultureInfo(_n_0_t_0, _n_0_t_9):
    @property
    def Calendar(self) -> Calendar:"""Calendar { get; } -> Calendar"""
    @property
    def CompareInfo(self) -> CompareInfo:"""CompareInfo { get; } -> CompareInfo"""
    @property
    def CultureTypes(self) -> CultureTypes:"""CultureTypes { get; } -> CultureTypes"""
    @property
    def CurrentCulture(self) -> CultureInfo:"""CurrentCulture { get; set; } -> CultureInfo"""
    @property
    def CurrentUICulture(self) -> CultureInfo:"""CurrentUICulture { get; set; } -> CultureInfo"""
    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo:"""DateTimeFormat { get; set; } -> DateTimeFormatInfo"""
    @property
    def DefaultThreadCurrentCulture(self) -> CultureInfo:"""DefaultThreadCurrentCulture { get; set; } -> CultureInfo"""
    @property
    def DefaultThreadCurrentUICulture(self) -> CultureInfo:"""DefaultThreadCurrentUICulture { get; set; } -> CultureInfo"""
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def EnglishName(self) -> str:"""EnglishName { get; } -> str"""
    @property
    def IetfLanguageTag(self) -> str:"""IetfLanguageTag { get; } -> str"""
    @property
    def InstalledUICulture(self) -> CultureInfo:"""InstalledUICulture { get; } -> CultureInfo"""
    @property
    def InvariantCulture(self) -> CultureInfo:"""InvariantCulture { get; } -> CultureInfo"""
    @property
    def IsNeutralCulture(self) -> bool:"""IsNeutralCulture { get; } -> bool"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def KeyboardLayoutId(self) -> int:"""KeyboardLayoutId { get; } -> int"""
    @property
    def LCID(self) -> int:"""LCID { get; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NativeName(self) -> str:"""NativeName { get; } -> str"""
    @property
    def NumberFormat(self) -> NumberFormatInfo:"""NumberFormat { get; set; } -> NumberFormatInfo"""
    @property
    def OptionalCalendars(self) -> _n_0_t_1[Calendar]:"""OptionalCalendars { get; } -> Array"""
    @property
    def Parent(self) -> CultureInfo:"""Parent { get; } -> CultureInfo"""
    @property
    def TextInfo(self) -> TextInfo:"""TextInfo { get; } -> TextInfo"""
    @property
    def ThreeLetterISOLanguageName(self) -> str:"""ThreeLetterISOLanguageName { get; } -> str"""
    @property
    def ThreeLetterWindowsLanguageName(self) -> str:"""ThreeLetterWindowsLanguageName { get; } -> str"""
    @property
    def TwoLetterISOLanguageName(self) -> str:"""TwoLetterISOLanguageName { get; } -> str"""
    @property
    def UseUserOverride(self) -> bool:"""UseUserOverride { get; } -> bool"""
    def __init__(self, culture: int, useUserOverride: bool) -> CultureInfo:...
    def __init__(self, culture: int) -> CultureInfo:...
    def __init__(self, name: str, useUserOverride: bool) -> CultureInfo:...
    def __init__(self, name: str) -> CultureInfo:...
    def ClearCachedData(self):...
    @staticmethod
    def CreateSpecificCulture(name: str) -> CultureInfo:...
    def GetConsoleFallbackUICulture(self) -> CultureInfo:...
    @staticmethod
    def GetCultureInfo(name: str, altName: str) -> CultureInfo:...
    @staticmethod
    def GetCultureInfo(name: str) -> CultureInfo:...
    @staticmethod
    def GetCultureInfo(culture: int) -> CultureInfo:...
    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name: str) -> CultureInfo:...
    @staticmethod
    def GetCultures(types: CultureTypes) -> _n_0_t_1[CultureInfo]:...
    @staticmethod
    def ReadOnly(ci: CultureInfo) -> CultureInfo:...
class CultureNotFoundException(_n_0_t_10, _n_4_t_1, _n_3_t_0):
    @property
    def InvalidCultureId(self) -> _n_0_t_11[int]:"""InvalidCultureId { get; } -> Nullable"""
    @property
    def InvalidCultureName(self) -> str:"""InvalidCultureName { get; } -> str"""
    def __init__(self, message: str, invalidCultureName: str, innerException: _n_0_t_12) -> CultureNotFoundException:...
    def __init__(self, paramName: str, invalidCultureName: str, message: str) -> CultureNotFoundException:...
    def __init__(self, message: str, invalidCultureId: int, innerException: _n_0_t_12) -> CultureNotFoundException:...
    def __init__(self, paramName: str, invalidCultureId: int, message: str) -> CultureNotFoundException:...
    def __init__(self, message: str, innerException: _n_0_t_12) -> CultureNotFoundException:...
    def __init__(self, paramName: str, message: str) -> CultureNotFoundException:...
    def __init__(self, message: str) -> CultureNotFoundException:...
    def __init__(self) -> CultureNotFoundException:...
class CultureTypes(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    AllCultures: int
    FrameworkCultures: int
    InstalledWin32Cultures: int
    NeutralCultures: int
    ReplacementCultures: int
    SpecificCultures: int
    UserCustomCulture: int
    value__: int
    WindowsOnlyCultures: int
class DateTimeFormatInfo(_n_0_t_0, _n_0_t_9):
    @property
    def AbbreviatedDayNames(self) -> _n_0_t_1[str]:"""AbbreviatedDayNames { get; set; } -> Array"""
    @property
    def AbbreviatedMonthGenitiveNames(self) -> _n_0_t_1[str]:"""AbbreviatedMonthGenitiveNames { get; set; } -> Array"""
    @property
    def AbbreviatedMonthNames(self) -> _n_0_t_1[str]:"""AbbreviatedMonthNames { get; set; } -> Array"""
    @property
    def AMDesignator(self) -> str:"""AMDesignator { get; set; } -> str"""
    @property
    def Calendar(self) -> Calendar:"""Calendar { get; set; } -> Calendar"""
    @property
    def CalendarWeekRule(self) -> CalendarWeekRule:"""CalendarWeekRule { get; set; } -> CalendarWeekRule"""
    @property
    def CurrentInfo(self) -> DateTimeFormatInfo:"""CurrentInfo { get; } -> DateTimeFormatInfo"""
    @property
    def DateSeparator(self) -> str:"""DateSeparator { get; set; } -> str"""
    @property
    def DayNames(self) -> _n_0_t_1[str]:"""DayNames { get; set; } -> Array"""
    @property
    def FirstDayOfWeek(self) -> _n_0_t_3:"""FirstDayOfWeek { get; set; } -> DayOfWeek"""
    @property
    def FullDateTimePattern(self) -> str:"""FullDateTimePattern { get; set; } -> str"""
    @property
    def InvariantInfo(self) -> DateTimeFormatInfo:"""InvariantInfo { get; } -> DateTimeFormatInfo"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def LongDatePattern(self) -> str:"""LongDatePattern { get; set; } -> str"""
    @property
    def LongTimePattern(self) -> str:"""LongTimePattern { get; set; } -> str"""
    @property
    def MonthDayPattern(self) -> str:"""MonthDayPattern { get; set; } -> str"""
    @property
    def MonthGenitiveNames(self) -> _n_0_t_1[str]:"""MonthGenitiveNames { get; set; } -> Array"""
    @property
    def MonthNames(self) -> _n_0_t_1[str]:"""MonthNames { get; set; } -> Array"""
    @property
    def NativeCalendarName(self) -> str:"""NativeCalendarName { get; } -> str"""
    @property
    def PMDesignator(self) -> str:"""PMDesignator { get; set; } -> str"""
    @property
    def RFC1123Pattern(self) -> str:"""RFC1123Pattern { get; } -> str"""
    @property
    def ShortDatePattern(self) -> str:"""ShortDatePattern { get; set; } -> str"""
    @property
    def ShortestDayNames(self) -> _n_0_t_1[str]:"""ShortestDayNames { get; set; } -> Array"""
    @property
    def ShortTimePattern(self) -> str:"""ShortTimePattern { get; set; } -> str"""
    @property
    def SortableDateTimePattern(self) -> str:"""SortableDateTimePattern { get; } -> str"""
    @property
    def TimeSeparator(self) -> str:"""TimeSeparator { get; set; } -> str"""
    @property
    def UniversalSortableDateTimePattern(self) -> str:"""UniversalSortableDateTimePattern { get; } -> str"""
    @property
    def YearMonthPattern(self) -> str:"""YearMonthPattern { get; set; } -> str"""
    def __init__(self) -> DateTimeFormatInfo:...
    def GetAbbreviatedDayName(self, dayofweek: _n_0_t_3) -> str:...
    def GetAbbreviatedEraName(self, era: int) -> str:...
    def GetAbbreviatedMonthName(self, month: int) -> str:...
    def GetAllDateTimePatterns(self) -> _n_0_t_1[str]:...
    def GetAllDateTimePatterns(self, format: _n_0_t_8) -> _n_0_t_1[str]:...
    def GetDayName(self, dayofweek: _n_0_t_3) -> str:...
    def GetEra(self, eraName: str) -> int:...
    def GetEraName(self, era: int) -> str:...
    @staticmethod
    def GetInstance(provider: _n_0_t_9) -> DateTimeFormatInfo:...
    def GetMonthName(self, month: int) -> str:...
    def GetShortestDayName(self, dayOfWeek: _n_0_t_3) -> str:...
    @staticmethod
    def ReadOnly(dtfi: DateTimeFormatInfo) -> DateTimeFormatInfo:...
    def SetAllDateTimePatterns(self, patterns: _n_0_t_1[str], format: _n_0_t_8):...
class DateTimeStyles(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    AdjustToUniversal: int
    AllowInnerWhite: int
    AllowLeadingWhite: int
    AllowTrailingWhite: int
    AllowWhiteSpaces: int
    AssumeLocal: int
    AssumeUniversal: int
    NoCurrentDateDefault: int
    _None: int
    RoundtripKind: int
    value__: int
class DaylightTime(object):
    @property
    def Delta(self) -> _n_0_t_13:"""Delta { get; } -> TimeSpan"""
    @property
    def End(self) -> _n_0_t_2:"""End { get; } -> DateTime"""
    @property
    def Start(self) -> _n_0_t_2:"""Start { get; } -> DateTime"""
    def __init__(self, start: _n_0_t_2, end: _n_0_t_2, delta: _n_0_t_13) -> DaylightTime:...
class DigitShapes(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    Context: int
    NativeNational: int
    _None: int
    value__: int
class EastAsianLunisolarCalendar(Calendar, _n_0_t_0):
    def GetCelestialStem(self, sexagenaryYear: int) -> int:...
    def GetSexagenaryYear(self, time: _n_0_t_2) -> int:...
    def GetTerrestrialBranch(self, sexagenaryYear: int) -> int:...
class GlobalizationExtensions(object):
    @staticmethod
    def GetStringComparer(compareInfo: CompareInfo, options: CompareOptions) -> _n_0_t_14:...
class GregorianCalendar(Calendar, _n_0_t_0):
    ADEra: int
    @property
    def CalendarType(self) -> GregorianCalendarTypes:"""CalendarType { get; set; } -> GregorianCalendarTypes"""
    def __init__(self) -> GregorianCalendar:...
    def __init__(self, type: GregorianCalendarTypes) -> GregorianCalendar:...
class GregorianCalendarTypes(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    Arabic: int
    Localized: int
    MiddleEastFrench: int
    TransliteratedEnglish: int
    TransliteratedFrench: int
    USEnglish: int
    value__: int
class HebrewCalendar(Calendar, _n_0_t_0):
    HebrewEra: int
    def __init__(self) -> HebrewCalendar:...
class HijriCalendar(Calendar, _n_0_t_0):
    HijriEra: int
    @property
    def HijriAdjustment(self) -> int:"""HijriAdjustment { get; set; } -> int"""
    def __init__(self) -> HijriCalendar:...
class IdnMapping(object):
    @property
    def AllowUnassigned(self) -> bool:"""AllowUnassigned { get; set; } -> bool"""
    @property
    def UseStd3AsciiRules(self) -> bool:"""UseStd3AsciiRules { get; set; } -> bool"""
    def __init__(self) -> IdnMapping:...
    def GetAscii(self, unicode: str, index: int, count: int) -> str:...
    def GetAscii(self, unicode: str, index: int) -> str:...
    def GetAscii(self, unicode: str) -> str:...
    def GetUnicode(self, ascii: str, index: int, count: int) -> str:...
    def GetUnicode(self, ascii: str, index: int) -> str:...
    def GetUnicode(self, ascii: str) -> str:...
class JapaneseCalendar(Calendar, _n_0_t_0):
    def __init__(self) -> JapaneseCalendar:...
class JapaneseLunisolarCalendar(EastAsianLunisolarCalendar, _n_0_t_0):
    JapaneseEra: int
    def __init__(self) -> JapaneseLunisolarCalendar:...
class JulianCalendar(Calendar, _n_0_t_0):
    JulianEra: int
    def __init__(self) -> JulianCalendar:...
class KoreanCalendar(Calendar, _n_0_t_0):
    KoreanEra: int
    def __init__(self) -> KoreanCalendar:...
class KoreanLunisolarCalendar(EastAsianLunisolarCalendar, _n_0_t_0):
    GregorianEra: int
    def __init__(self) -> KoreanLunisolarCalendar:...
class NumberFormatInfo(_n_0_t_0, _n_0_t_9):
    @property
    def CurrencyDecimalDigits(self) -> int:"""CurrencyDecimalDigits { get; set; } -> int"""
    @property
    def CurrencyDecimalSeparator(self) -> str:"""CurrencyDecimalSeparator { get; set; } -> str"""
    @property
    def CurrencyGroupSeparator(self) -> str:"""CurrencyGroupSeparator { get; set; } -> str"""
    @property
    def CurrencyGroupSizes(self) -> _n_0_t_1[int]:"""CurrencyGroupSizes { get; set; } -> Array"""
    @property
    def CurrencyNegativePattern(self) -> int:"""CurrencyNegativePattern { get; set; } -> int"""
    @property
    def CurrencyPositivePattern(self) -> int:"""CurrencyPositivePattern { get; set; } -> int"""
    @property
    def CurrencySymbol(self) -> str:"""CurrencySymbol { get; set; } -> str"""
    @property
    def CurrentInfo(self) -> NumberFormatInfo:"""CurrentInfo { get; } -> NumberFormatInfo"""
    @property
    def DigitSubstitution(self) -> DigitShapes:"""DigitSubstitution { get; set; } -> DigitShapes"""
    @property
    def InvariantInfo(self) -> NumberFormatInfo:"""InvariantInfo { get; } -> NumberFormatInfo"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def NaNSymbol(self) -> str:"""NaNSymbol { get; set; } -> str"""
    @property
    def NativeDigits(self) -> _n_0_t_1[str]:"""NativeDigits { get; set; } -> Array"""
    @property
    def NegativeInfinitySymbol(self) -> str:"""NegativeInfinitySymbol { get; set; } -> str"""
    @property
    def NegativeSign(self) -> str:"""NegativeSign { get; set; } -> str"""
    @property
    def NumberDecimalDigits(self) -> int:"""NumberDecimalDigits { get; set; } -> int"""
    @property
    def NumberDecimalSeparator(self) -> str:"""NumberDecimalSeparator { get; set; } -> str"""
    @property
    def NumberGroupSeparator(self) -> str:"""NumberGroupSeparator { get; set; } -> str"""
    @property
    def NumberGroupSizes(self) -> _n_0_t_1[int]:"""NumberGroupSizes { get; set; } -> Array"""
    @property
    def NumberNegativePattern(self) -> int:"""NumberNegativePattern { get; set; } -> int"""
    @property
    def PercentDecimalDigits(self) -> int:"""PercentDecimalDigits { get; set; } -> int"""
    @property
    def PercentDecimalSeparator(self) -> str:"""PercentDecimalSeparator { get; set; } -> str"""
    @property
    def PercentGroupSeparator(self) -> str:"""PercentGroupSeparator { get; set; } -> str"""
    @property
    def PercentGroupSizes(self) -> _n_0_t_1[int]:"""PercentGroupSizes { get; set; } -> Array"""
    @property
    def PercentNegativePattern(self) -> int:"""PercentNegativePattern { get; set; } -> int"""
    @property
    def PercentPositivePattern(self) -> int:"""PercentPositivePattern { get; set; } -> int"""
    @property
    def PercentSymbol(self) -> str:"""PercentSymbol { get; set; } -> str"""
    @property
    def PerMilleSymbol(self) -> str:"""PerMilleSymbol { get; set; } -> str"""
    @property
    def PositiveInfinitySymbol(self) -> str:"""PositiveInfinitySymbol { get; set; } -> str"""
    @property
    def PositiveSign(self) -> str:"""PositiveSign { get; set; } -> str"""
    def __init__(self) -> NumberFormatInfo:...
    @staticmethod
    def GetInstance(formatProvider: _n_0_t_9) -> NumberFormatInfo:...
    @staticmethod
    def ReadOnly(nfi: NumberFormatInfo) -> NumberFormatInfo:...
class NumberStyles(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    AllowCurrencySymbol: int
    AllowDecimalPoint: int
    AllowExponent: int
    AllowHexSpecifier: int
    AllowLeadingSign: int
    AllowLeadingWhite: int
    AllowParentheses: int
    AllowThousands: int
    AllowTrailingSign: int
    AllowTrailingWhite: int
    Any: int
    Currency: int
    Float: int
    HexNumber: int
    Integer: int
    _None: int
    Number: int
    value__: int
class PersianCalendar(Calendar, _n_0_t_0):
    PersianEra: int
    def __init__(self) -> PersianCalendar:...
class RegionInfo(object):
    @property
    def CurrencyEnglishName(self) -> str:"""CurrencyEnglishName { get; } -> str"""
    @property
    def CurrencyNativeName(self) -> str:"""CurrencyNativeName { get; } -> str"""
    @property
    def CurrencySymbol(self) -> str:"""CurrencySymbol { get; } -> str"""
    @property
    def CurrentRegion(self) -> RegionInfo:"""CurrentRegion { get; } -> RegionInfo"""
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def EnglishName(self) -> str:"""EnglishName { get; } -> str"""
    @property
    def GeoId(self) -> int:"""GeoId { get; } -> int"""
    @property
    def IsMetric(self) -> bool:"""IsMetric { get; } -> bool"""
    @property
    def ISOCurrencySymbol(self) -> str:"""ISOCurrencySymbol { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NativeName(self) -> str:"""NativeName { get; } -> str"""
    @property
    def ThreeLetterISORegionName(self) -> str:"""ThreeLetterISORegionName { get; } -> str"""
    @property
    def ThreeLetterWindowsRegionName(self) -> str:"""ThreeLetterWindowsRegionName { get; } -> str"""
    @property
    def TwoLetterISORegionName(self) -> str:"""TwoLetterISORegionName { get; } -> str"""
    def __init__(self, culture: int) -> RegionInfo:...
    def __init__(self, name: str) -> RegionInfo:...
class SortKey(object):
    @property
    def KeyData(self) -> _n_0_t_1[_n_0_t_15]:"""KeyData { get; } -> Array"""
    @property
    def OriginalString(self) -> str:"""OriginalString { get; } -> str"""
    @staticmethod
    def Compare(sortkey1: SortKey, sortkey2: SortKey) -> int:...
class SortVersion(_n_0_t_16[SortVersion]):
    @property
    def FullVersion(self) -> int:"""FullVersion { get; } -> int"""
    @property
    def SortId(self) -> _n_0_t_17:"""SortId { get; } -> Guid"""
    def __init__(self, fullVersion: int, sortId: _n_0_t_17) -> SortVersion:...
class StringInfo(object):
    @property
    def LengthInTextElements(self) -> int:"""LengthInTextElements { get; } -> int"""
    @property
    def String(self) -> str:"""String { get; set; } -> str"""
    def __init__(self, value: str) -> StringInfo:...
    def __init__(self) -> StringInfo:...
    @staticmethod
    def GetNextTextElement(str: str, index: int) -> str:...
    @staticmethod
    def GetNextTextElement(str: str) -> str:...
    @staticmethod
    def GetTextElementEnumerator(str: str, index: int) -> TextElementEnumerator:...
    @staticmethod
    def GetTextElementEnumerator(str: str) -> TextElementEnumerator:...
    @staticmethod
    def ParseCombiningCharacters(str: str) -> _n_0_t_1[int]:...
    def SubstringByTextElements(self, startingTextElement: int, lengthInTextElements: int) -> str:...
    def SubstringByTextElements(self, startingTextElement: int) -> str:...
class TaiwanCalendar(Calendar, _n_0_t_0):
    def __init__(self) -> TaiwanCalendar:...
class TaiwanLunisolarCalendar(EastAsianLunisolarCalendar, _n_0_t_0):
    def __init__(self) -> TaiwanLunisolarCalendar:...
class TextElementEnumerator(_n_1_t_0):
    @property
    def ElementIndex(self) -> int:"""ElementIndex { get; } -> int"""
    def GetTextElement(self) -> str:...
class TextInfo(_n_0_t_0, _n_4_t_0):
    @property
    def ANSICodePage(self) -> int:"""ANSICodePage { get; } -> int"""
    @property
    def CultureName(self) -> str:"""CultureName { get; } -> str"""
    @property
    def EBCDICCodePage(self) -> int:"""EBCDICCodePage { get; } -> int"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def IsRightToLeft(self) -> bool:"""IsRightToLeft { get; } -> bool"""
    @property
    def LCID(self) -> int:"""LCID { get; } -> int"""
    @property
    def ListSeparator(self) -> str:"""ListSeparator { get; set; } -> str"""
    @property
    def MacCodePage(self) -> int:"""MacCodePage { get; } -> int"""
    @property
    def OEMCodePage(self) -> int:"""OEMCodePage { get; } -> int"""
    @staticmethod
    def ReadOnly(textInfo: TextInfo) -> TextInfo:...
    def ToLower(self, str: str) -> str:...
    def ToLower(self, c: _n_0_t_8) -> _n_0_t_8:...
    def ToTitleCase(self, str: str) -> str:...
    def ToUpper(self, str: str) -> str:...
    def ToUpper(self, c: _n_0_t_8) -> _n_0_t_8:...
class ThaiBuddhistCalendar(Calendar, _n_0_t_0):
    ThaiBuddhistEra: int
    def __init__(self) -> ThaiBuddhistCalendar:...
class TimeSpanStyles(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    AssumeNegative: int
    _None: int
    value__: int
class UmAlQuraCalendar(Calendar, _n_0_t_0):
    UmAlQuraEra: int
    def __init__(self) -> UmAlQuraCalendar:...
class UnicodeCategory(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    ClosePunctuation: int
    ConnectorPunctuation: int
    Control: int
    CurrencySymbol: int
    DashPunctuation: int
    DecimalDigitNumber: int
    EnclosingMark: int
    FinalQuotePunctuation: int
    Format: int
    InitialQuotePunctuation: int
    LetterNumber: int
    LineSeparator: int
    LowercaseLetter: int
    MathSymbol: int
    ModifierLetter: int
    ModifierSymbol: int
    NonSpacingMark: int
    OpenPunctuation: int
    OtherLetter: int
    OtherNotAssigned: int
    OtherNumber: int
    OtherPunctuation: int
    OtherSymbol: int
    ParagraphSeparator: int
    PrivateUse: int
    SpaceSeparator: int
    SpacingCombiningMark: int
    Surrogate: int
    TitlecaseLetter: int
    UppercaseLetter: int
    value__: int

class ResumeImportError(Exception):
    """Base exception for AI resume import."""


class ResumeParsingError(ResumeImportError):
    """Raised when resume parsing fails."""


class GeminiAPIError(ResumeImportError):
    """Raised when Gemini API fails."""


class DataMappingError(ResumeImportError):
    """Raised when database mapping fails."""


class InvalidResumeError(ResumeImportError):
    """Raised when uploaded resume is invalid."""
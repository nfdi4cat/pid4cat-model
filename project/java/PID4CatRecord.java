package None;

import java.util.List;
import lombok.*;






/**
  Represents a PID4CatRecord
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PID4CatRecord  {

  private String id;
  private String landingPageUrl;
  private String status;
  private String pidSchemaVersion;
  private String license;
  private String curationContactEmail;
  private ResourceInfo resourceInfo;
  private List<PID4CatRelation> relatedIdentifiers;
  private List<LogRecord> changeLog;

}
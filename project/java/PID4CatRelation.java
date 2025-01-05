package None;

import java.util.List;
import lombok.*;






/**
  A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PID4CatRelation  {

  private String relationType;
  private String relatedIdentifier;
  private String datetimeLog;

}
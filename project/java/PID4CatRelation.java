package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  Data class for a relation to another resource identified by a pid4cat handle or another PID type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Pid4CatRelation  {

  private String relationType;
  private RelatedIdentifier relatedIdentifier;
  private ZonedDateTime datetimeLog;

}

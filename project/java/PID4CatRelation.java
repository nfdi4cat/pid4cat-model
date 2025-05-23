package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


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
